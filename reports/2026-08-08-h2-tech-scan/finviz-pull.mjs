// Finviz fundamentals puller (fixed parser) — 2026-08-08
import fs from "node:fs";
const DIR = "F:/ai-berkshire/reports/2026-08-08-h2-tech-scan";
const UA = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36","Accept":"text/html,*/*","Accept-Language":"en-US,en;q=0.9"};
let rounds = [];
try { rounds = fs.readFileSync(DIR+"/data/rounds.jsonl","utf8").trim().split("\n").map(l=>JSON.parse(l)); } catch(e){}
let roundId = rounds.length;
function logRound(r){ rounds.push({round: ++roundId, ts: Date.now(), ...r}); }
const sleep = ms => new Promise(res=>setTimeout(res,ms));

function stripTags(s){ return s.replace(/<svg[\s\S]*?<\/svg>/g,"").replace(/<[^>]+>/g,"").trim(); }
function parseFinvizTable(html){
  const headers = [...html.matchAll(/<th[^>]*>([\s\S]*?)<\/th>/g)].map(m=>stripTags(m[1]));
  const start = html.indexOf("</thead>");
  const end = html.indexOf("</table>", start);
  const body = start >= 0 ? html.slice(start, end > start ? end : undefined) : html;
  const rows = [];
  for (const rm of body.matchAll(/<tr[^>]*>([\s\S]*?)<\/tr>/g)){
    const cells = [...rm[1].matchAll(/<td[^>]*>([\s\S]*?)<\/td>/g)].map(m=>stripTags(m[1]));
    if (cells.length >= 3) rows.push(cells);
  }
  return {headers, rows};
}
async function fetchPage(view, sector, offset){
  const u = `https://finviz.com/screener.ashx?v=${view}&f=${sector},cap_midover&o=-marketcap&r=${offset}`;
  for (let a=0;a<3;a++){
    try {
      const r = await fetch(u,{headers:UA});
      if (r.status!==200) throw new Error("http "+r.status);
      return parseFinvizTable(await r.text());
    } catch(e){ console.log("retry", u, e.message); await sleep(1800); }
  }
  return {headers:[],rows:[]};
}
const fv = {};
async function pullAll(view, sector, fieldsMap){
  let offset=1, pages=0;
  while (offset<1500 && pages<75){
    const {headers, rows} = await fetchPage(view, sector, offset);
    if (!rows.length){ break; }
    pages++;
    const idx = {};
    headers.forEach((h,i)=>idx[h]=i);
    for (const cells of rows){
      const ti = idx["Ticker"]; if (ti===undefined) continue;
      const t = cells[ti]; if (!t) continue;
      if (!fv[t]) fv[t]={};
      for (const [h,key] of fieldsMap){
        const i2 = idx[h];
        if (i2!==undefined && cells[i2]!==undefined){
          fv[t][key]=cells[i2];
          logRound({type:"metric", ticker:t, field:key, value:cells[i2]});
        }
      }
    }
    console.log(`${sector} v=${view} page r=${offset}: ${rows.length} rows`);
    if (rows.length<20) break;
    offset+=20;
    await sleep(400);
  }
  return pages;
}
const valMap = [["Market Cap","mcap"],["P/E","pe"],["Forward P/E","fpe"],["PEG","peg"],["P/S","ps"],["P/B","pb"],["P/FCF","pfcf"],["EPS This Y","eps_this_y_pct"],["EPS Next Y","eps_next_y_pct"],["EPS Past 5Y","eps_5y_pct"],["EPS Next 5Y","eps_next5y_pct"],["Sales Past 5Y","sales_5y_pct"],["Price","price"],["Change","chg"]];
const perfMap = [["Perf Week","perf_week"],["Perf Month","perf_month"],["Perf Quart","perf_quart"],["Perf Half","perf_half"],["Perf Year","perf_year"],["Perf YTD","perf_ytd"],["52W High","w52h"],["52W Low","w52l"],["Recom","recom"],["Avg Volume","avgvol"],["Volatility W","volw"],["Volatility M","volm"]];
console.log("pages tech val:", await pullAll(121,"sec_technology",valMap));
console.log("pages comm val:", await pullAll(121,"sec_communication_services",valMap));
console.log("pages tech perf:", await pullAll(141,"sec_technology",perfMap));
console.log("pages comm perf:", await pullAll(141,"sec_communication_services",perfMap));
fs.writeFileSync(DIR+"/data/finviz-merged.json", JSON.stringify(fv,null,1));
const screened = JSON.parse(fs.readFileSync(DIR+"/data/screened.json","utf8"));
const merged = screened.map(s=>({ ...s, fv: fv[s.symbol]||null }));
fs.writeFileSync(DIR+"/data/merged.json", JSON.stringify(merged,null,1));
fs.writeFileSync(DIR+"/data/rounds.jsonl", rounds.map(r=>JSON.stringify(r)).join("\n")+"\n");
console.log("tickers with finviz:", Object.keys(fv).length, "| total rounds:", rounds.length);
