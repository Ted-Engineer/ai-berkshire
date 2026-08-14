// industry-pull.mjs — Finviz tech sector ticker->industry map (v=111)
import fs from "node:fs";
const DIR = "F:/ai-berkshire/reports/2026-08-08-h2-tech-scan/data";
const UA = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36","Accept":"text/html,*/*","Accept-Language":"en-US,en;q=0.9"};
const sleep = ms => new Promise(res=>setTimeout(res,ms));
function stripTags(s){ return s.replace(/<svg[\s\S]*?<\/svg>/g,"").replace(/<[^>]+>/g,"").trim(); }
function parseTable(html){
  const headers = [...html.matchAll(/<th[^>]*>([\s\S]*?)<\/th>/g)].map(m=>stripTags(m[1]));
  const start = html.indexOf("</thead>");
  const end = html.indexOf("</table>", start);
  const body = html.slice(start, end>start?end:undefined);
  const rows=[];
  for (const rm of body.matchAll(/<tr[^>]*>([\s\S]*?)<\/tr>/g)){
    const cells=[...rm[1].matchAll(/<td[^>]*>([\s\S]*?)<\/td>/g)].map(m=>stripTags(m[1]));
    if(cells.length>=3) rows.push(cells);
  }
  return {headers, rows};
}
const map = {};
async function pull(sector){
  let offset=1,pages=0;
  while(offset<1500 && pages<80){
    const u = `https://finviz.com/screener.ashx?v=111&f=${sector}&o=-marketcap&r=${offset}`;
    let ok=false;
    for(let a=0;a<3&&!ok;a++){
      try{
        const r=await fetch(u,{headers:UA});
        if(r.status!==200) throw new Error("http "+r.status);
        const {headers,rows}=parseTable(await r.text());
        const idx={}; headers.forEach((h,i)=>idx[h]=i);
        for(const c of rows){
          let t=c[idx["Ticker"]]; if(!t) continue;
          if(t.length>=2&&t.slice(0,1).toUpperCase()===t.slice(1,2).toUpperCase()) t=t.slice(1);
          map[t]={sector: sector.replace("sec_",""), industry: c[idx["Industry"]]||"", company: c[idx["Company"]]||""};
        }
        console.log(sector, "r="+offset, rows.length, "rows");
        ok=true;
        if(rows.length<20){ offset=9999; break; }
      }catch(e){ console.log("retry",e.message); await sleep(1500); }
    }
    offset+=20; pages++;
    await sleep(350);
  }
}
await pull("sec_technology");
await pull("sec_communication_services");
fs.writeFileSync(DIR+"/industry-map.json", JSON.stringify(map,null,1));
console.log("industry map entries:", Object.keys(map).length);
