// 全美股科技板块遍历流水线 (2026-08-08)
import fs from "node:fs";
const DIR = "F:/ai-berkshire/reports/2026-08-08-h2-tech-scan";
const UA = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36","Accept":"text/html,application/json,*/*","Accept-Language":"en-US,en;q=0.9"};
const rounds = [];
let roundId = 0;
function logRound(r){ rounds.push({round: ++roundId, ts: Date.now(), ...r}); }
const sleep = ms => new Promise(res=>setTimeout(res,ms));

// ---------- Step 1: Universe (Nasdaq API full technology sector) ----------
async function pullNasdaq(sector){
  const u = `https://api.nasdaq.com/api/screener/stocks?tableonly=true&limit=3000&offset=0&sector=${sector}`;
  const r = await fetch(u,{headers:UA}); const j = await r.json();
  return j?.data?.table?.rows || [];
}
const tech = await pullNasdaq("technology");
console.log("nasdaq tech rows:", tech.length);
// manual adds: communication-services internet giants (Nasdaq API slug unavailable)
const manualAdds = ["GOOGL","GOOG","META","NFLX"].map(s=>({symbol:s,name:"manual-add communication services",lastsale:"",netchange:"",pctchange:"",marketCap:"",manual:true}));
const universe = [...tech, ...manualAdds];
fs.writeFileSync(DIR+"/data/universe-tech.json", JSON.stringify({asof:"2026-08-07 close", source:"api.nasdaq.com + manual comm-services adds", count: universe.length, rows: universe}, null, 1));

// ---------- Step 2: Screen every stock (round logging) ----------
function parseMoney(s){ if(!s) return null; const t = String(s).replace(/[$,]/g,""); const v = parseFloat(t); return isNaN(v)? null : v; }
const screened = [];
for (const row of universe){
  const sym = row.symbol || "";
  const name = row.name || "";
  const mcap = parseMoney(row.marketCap);
  const price = parseMoney(row.lastsale);
  const isCommon = !/\b(Right|Warrant|Unit|Rights)\b/i.test(name) && !sym.includes(".") ; // dots = classes/rights on nasdaq
  const bigEnough = mcap !== null && mcap >= 2e9;
  const priceOk = price !== null && price >= 1;
  const pass = isCommon && bigEnough && priceOk;
  logRound({type:"screen", ticker:sym, mcap_b: mcap? +(mcap/1e9).toFixed(2):null, checks:{isCommon, bigEnough, priceOk}, pass});
  if (pass) screened.push({symbol:sym, name, price, mcap_b:+(mcap/1e9).toFixed(2), pctchange: row.pctchange});
}
console.log("screened (mcap>=2B, common, price>=1):", screened.length);
fs.writeFileSync(DIR+"/data/screened.json", JSON.stringify(screened, null, 1));

// ---------- Step 3: Finviz fundamentals (v=121 valuation, v=141 performance) ----------
function parseFinvizTable(html){
  const thead = html.match(/<thead>([\s\S]*?)<\/thead>/);
  const headers = thead ? [...thead[1].matchAll(/<th[^>]*>([\s\S]*?)<\/th>/g)].map(m=>m[1].replace(/<svg[\s\S]*?<\/svg>/g,"").replace(/<[^>]+>/g,"").trim()) : [];
  const tbody = html.split(/<tbody[^>]*>/)[1] || "";
  const rows = [];
  for (const rm of tbody.matchAll(/<tr[^>]*>([\s\S]*?)<\/tr>/g)){
    const cells = [...rm[1].matchAll(/<td[^>]*>([\s\S]*?)<\/td>/g)].map(m=>m[1].replace(/<[^>]+>/g,"").trim());
    if (cells.length >= 3) rows.push(cells);
  }
  return {headers, rows};
}
async function fetchFinviz(view, sector, offset){
  const u = `https://finviz.com/screener.ashx?v=${view}&f=${sector},cap_midover&o=-marketcap&r=${offset}`;
  for (let attempt=0; attempt<3; attempt++){
    try {
      const r = await fetch(u, {headers:UA});
      if (r.status !== 200) throw new Error("status "+r.status);
      const html = await r.text();
      return parseFinvizTable(html);
    } catch(e){ await sleep(1500); }
  }
  return {headers:[], rows:[]};
}
const fv = {}; // ticker -> fields
async function pullAll(view, sector, fieldsMap){
  let offset = 1, pages = 0;
  while (offset < 1200 && pages < 60){
    const {headers, rows} = await fetchFinviz(view, sector, offset);
    if (!rows.length) break;
    pages++;
    for (const cells of rows){
      const rec = {};
      headers.forEach((h,i)=>{ rec[h] = cells[i]; });
      const t = rec["Ticker"];
      if (!t) continue;
      if (!fv[t]) fv[t] = {};
      for (const [h, key] of fieldsMap){
        if (rec[h] !== undefined){ fv[t][key] = rec[h]; }
      }
      // metric rounds: log each field value as an evaluation round
      for (const [h,key] of fieldsMap){
        if (rec[h] !== undefined) logRound({type:"metric", ticker:t, field:key, value:rec[h]});
      }
    }
    if (rows.length < 20) break;
    offset += 20;
    await sleep(350);
  }
  return pages;
}
const valMap = [["Market Cap","mcap"],["P/E","pe"],["Forward P/E","fpe"],["PEG","peg"],["P/S","ps"],["P/B","pb"],["P/FCF","pfcf"],["EPS This Y","eps_this_y_pct"],["EPS Next Y","eps_next_y_pct"],["EPS Past 5Y","eps_5y_pct"],["EPS Next 5Y","eps_next5y_pct"],["Sales Past 5Y","sales_5y_pct"],["Price","price"],["Change","chg"]];
const perfMap = [["Perf Week","perf_week"],["Perf Month","perf_month"],["Perf Quart","perf_quart"],["Perf Half","perf_half"],["Perf Year","perf_year"],["Perf YTD","perf_ytd"],["52W High","w52h"],["52W Low","w52l"],["Volatility W","vol"],["Recom","recom"],["Avg Volume","avgvol"]];
console.log("finviz tech valuation pages:", await pullAll(121,"sec_technology",valMap));
console.log("finviz comm valuation pages:", await pullAll(121,"sec_communication_services",valMap));
console.log("finviz tech performance pages:", await pullAll(141,"sec_technology",perfMap));
console.log("finviz comm performance pages:", await pullAll(141,"sec_communication_services",perfMap));
fs.writeFileSync(DIR+"/data/finviz-merged.json", JSON.stringify(fv, null, 1));

// ---------- Step 4: Merge + output ----------
const merged = screened.map(s => ({...s, fv: fv[s.symbol] || null}));
fs.writeFileSync(DIR+"/data/merged.json", JSON.stringify(merged, null, 1));
fs.writeFileSync(DIR+"/data/rounds.jsonl", rounds.map(r=>JSON.stringify(r)).join("\n") + "\n");
console.log("TOTAL ROUNDS LOGGED:", rounds.length);
console.log("merged count:", merged.length, "with finviz data:", merged.filter(m=>m.fv && m.fv.pe!==undefined).length);
