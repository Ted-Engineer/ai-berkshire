// tournament2.mjs — fixed tech membership; re-run tournament
import fs from "node:fs";
const DIR = "F:/ai-berkshire/reports/2026-08-08-h2-tech-scan/data";
let rounds = fs.readFileSync(DIR+"/rounds.jsonl","utf8").trim().split("\n").map(l=>JSON.parse(l));
let roundId = rounds.length;
const logRound = r => rounds.push({round:++roundId, ts:Date.now(), ...r});

const indMap = JSON.parse(fs.readFileSync(DIR+"/industry-map.json","utf8"));
const uni = JSON.parse(fs.readFileSync(DIR+"/universe-tech.json","utf8"));
const nasdaqTech = new Set(uni.rows.map(r=>r.symbol));
const pool = JSON.parse(fs.readFileSync(DIR+"/scores.json","utf8"));

const TECH_INDUSTRIES = new Set(["Software - Application","Software - Infrastructure","Semiconductors","Semiconductor Equipment & Materials","Communication Equipment","Computer Hardware","Consumer Electronics","Electronic Components","Information Technology Services","Scientific & Technical Instruments","Electronic Gaming & Multimedia","Internet Content & Information"]);
const curated = ["VRT","GEV","TLN","EME","FIX","MOD","BE","PWR","OKLO","SMR","LEU","BWXT","VST","CEG","NRG","STRL","AAON","GOOGL","GOOG","META","NFLX","SKHY"];
const isTech = t => nasdaqTech.has(t) || (indMap[t] && TECH_INDUSTRIES.has(indMap[t].industry)) || (indMap[t] && indMap[t].sector==="technology") || curated.includes(t);
const techPool = pool.filter(p=>isTech(p.ticker));
techPool.sort((a,b)=>b.scores.composite-a.scores.composite);
console.log("tech pool:", techPool.length);
fs.writeFileSync(DIR+"/tech-pool.json", JSON.stringify(techPool,null,1));

const indCount = {};
techPool.slice(0,120).forEach(p=>{ const ind=(indMap[p.ticker]||{}).industry||"unknown"; indCount[ind]=(indCount[ind]||0)+1; });
console.log("\nindustry distribution of tech top 120:");
Object.entries(indCount).sort((a,b)=>b[1]-a[1]).forEach(([k,v])=>console.log(`  ${v.toString().padStart(3)}  ${k}`));

const N = 150;
const arena = techPool.slice(0,N).map(p=>({ ...p, wins:0, losses:0 }));
const pairLog = [];
let pairId = 0;
function reason(a,b){
  const parts=[]; const sa=a.scores, sb=b.scores;
  if (Math.abs(sa.valuation-sb.valuation)>0.15) parts.push(`估值(fPE ${a.fpe??"-"} vs ${b.fpe??"-"}, PEG ${a.peg??"-"} vs ${b.peg??"-"}):Δ${Math.abs(sa.valuation-sb.valuation).toFixed(2)}`);
  if (Math.abs(sa.growth-sb.growth)>0.12) parts.push(`增长(EPSny ${a.epsNextY??"-"}% vs ${b.epsNextY??"-"}%):Δ${Math.abs(sa.growth-sb.growth).toFixed(2)}`);
  if (Math.abs(sa.momentum-sb.momentum)>0.12) parts.push(`动量(YTD ${a.ytd??"-"}% vs ${b.ytd??"-"}%):Δ${Math.abs(sa.momentum-sb.momentum).toFixed(2)}`);
  if (!parts.length) parts.push(`综合微弱优势 Δ${(sa.composite-sb.composite).toFixed(2)}`);
  return parts.join("; ");
}
for (let i=0;i<arena.length;i++){
  for (let j=i+1;j<arena.length;j++){
    const a=arena[i], b=arena[j];
    const winner = a.scores.composite>=b.scores.composite ? a.ticker : b.ticker;
    const w = winner===a.ticker? a:b, l = winner===a.ticker? b:a;
    pairLog.push({pair:++pairId, a:a.ticker, b:b.ticker, winner, loser:l.ticker, margin:+(Math.abs(a.scores.composite-b.scores.composite)).toFixed(2), reason:reason(w,l)});
    logRound({type:"pairwise2", a:a.ticker, b:b.ticker, winner});
    if(winner===a.ticker){a.wins++;b.losses++;} else {b.wins++;a.losses++;}
  }
}
fs.writeFileSync(DIR+"/pairwise2.jsonl", pairLog.map(p=>JSON.stringify(p)).join("\n")+"\n");
console.log("\nround-robin comparisons:", pairLog.length);
let arr=[...arena], pass=0, swapped=true;
while(swapped&&pass<80){ swapped=false; pass++; for(let k=0;k<arr.length-1;k++){ if(arr[k].scores.composite<arr[k+1].scores.composite){[arr[k],arr[k+1]]=[arr[k+1],arr[k]];swapped=true;logRound({type:"bubble-swap2",pass,tickers:[arr[k+1].ticker,arr[k].ticker]});} } }
const ranking = arr.map((p,i)=>({rank:i+1, ticker:p.ticker, composite:p.scores.composite, wins:p.wins, losses:p.losses, fpe:p.fpe, peg:p.peg, pfcf:p.pfcf, epsThisY:p.epsThisY, epsNextY:p.epsNextY, ytd:p.ytd, yr:p.yr, quart:p.quart, mcap_b:p.mcap_b, industry:(indMap[p.ticker]||{}).industry||""}));
fs.writeFileSync(DIR+"/ranking.json", JSON.stringify(ranking,null,1));
fs.writeFileSync(DIR+"/rounds.jsonl", rounds.map(r=>JSON.stringify(r)).join("\n")+"\n");
console.log("bubble passes:", pass, "| TOTAL ROUNDS:", rounds.length);
console.log("\nTOP 45 RANKING:");
ranking.slice(0,45).forEach(r=>console.log(`#${String(r.rank).padStart(2)} ${r.ticker.padEnd(6)} comp=${String(r.composite).padStart(6)} W${String(r.wins).padStart(3)} fPE=${String(r.fpe??"-").padStart(6)} PEG=${String(r.peg??"-").padStart(5)} EPSny=${String(r.epsNextY??"-").padStart(7)}% YTD=${String(r.ytd??"-").padStart(7)}% mcap=$${String(r.mcap_b).padStart(7)}B [${r.industry}]`));
