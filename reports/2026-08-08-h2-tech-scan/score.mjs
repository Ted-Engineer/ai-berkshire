// score.mjs — 全市场科技股量化评分 + 两两比较锦标赛 (2026-08-08)
import fs from "node:fs";
const DIR = "F:/ai-berkshire/reports/2026-08-08-h2-tech-scan/data";
let rounds = [];
try { rounds = fs.readFileSync(DIR+"/rounds.jsonl","utf8").trim().split("\n").map(l=>JSON.parse(l)); } catch(e){}
let roundId = rounds.length;
const logRound = r => rounds.push({round:++roundId, ts:Date.now(), ...r});

const fv = JSON.parse(fs.readFileSync(DIR+"/finviz-fixed.json","utf8"));
const num = s => { if(!s || s==="-") return null; const v=parseFloat(String(s).replace(/[%,]/g,"")); return isNaN(v)?null:v; };
const mcapNum = s => { if(!s) return null; const m=String(s).match(/([\d.]+)([BMKT]?)/); if(!m) return null; const v=parseFloat(m[1]); const mult={B:1e9,M:1e6,K:1e3,T:1e12}[m[2]]||1; return v*mult; };
const clip=(x,a,b)=>Math.max(a,Math.min(b,x));

const pool=[];
for (const [t,v] of Object.entries(fv)){
  const mc = mcapNum(v.mcap);
  const price = num(v.price);
  const pass = mc!==null && mc>=2e9 && price!==null && price>=1;
  logRound({type:"screen2", ticker:t, mcap_b: mc?+(mc/1e9).toFixed(2):null, pass});
  if(!pass) continue;
  const epsThisY=num(v.eps_this_y_pct), epsNextY=num(v.eps_next_y_pct), epsN5Y=num(v.eps_next5y_pct);
  const peg=num(v.peg), fpe=num(v.fpe), pfcf=num(v.pfcf);
  const ytd=num(v.perf_ytd), yr=num(v.perf_year), quart=num(v.perf_quart), month=num(v.perf_month);
  const growth = (epsNextY===null&&epsThisY===null)?0:
    0.45*clip((epsNextY??0),0,200)/200 + 0.35*clip((epsThisY??0),0,300)/300 + 0.20*clip((epsN5Y??0),0,60)/60;
  const pegScore = peg===null?0:clip((1.1-peg)/0.8,0,1);
  const fpeScore = fpe===null?0:(fpe<=8?1:fpe<=12?0.85:fpe<=16?0.7:fpe<=20?0.55:fpe<=25?0.4:fpe<=32?0.25:fpe<=45?0.1:0.03);
  const valuation = peg===null ? fpeScore*0.7 : 0.6*pegScore+0.4*fpeScore;
  const ytdScore = ytd===null?0.4:(ytd<=-30?0.15:ytd<0?0.3:ytd<30?0.55:ytd<80?0.8:ytd<160?1.0:ytd<300?0.75:0.35);
  const yrScore = yr===null?0.4:(yr<=-40?0.15:yr<0?0.3:yr<60?0.55:yr<150?0.8:yr<300?1.0:yr<600?0.7:0.3);
  const momentum = 0.7*ytdScore+0.3*yrScore;
  const size = mc>=200e9?1:mc>=50e9?0.9:mc>=20e9?0.75:mc>=10e9?0.6:0.45;
  const fcfScore = pfcf===null?0.3:(pfcf<=12?1:pfcf<=20?0.8:pfcf<=30?0.6:pfcf<=45?0.4:pfcf<=80?0.2:0.05);
  const composite = 100*(0.30*growth+0.32*valuation+0.22*momentum+0.08*size+0.08*fcfScore);
  pool.push({ticker:t, price, mcap_b:+(mc/1e9).toFixed(2), pe:num(v.pe), fpe, peg, pfcf, epsThisY, epsNextY, epsN5Y, ytd, yr, quart, month, sales5y:num(v.sales_5y_pct), scores:{growth:+growth.toFixed(3), valuation:+valuation.toFixed(3), momentum:+momentum.toFixed(3), size, fcf:fcfScore, composite:+composite.toFixed(2)}});
  logRound({type:"score", ticker:t, composite:+composite.toFixed(2)});
}
pool.sort((a,b)=>b.scores.composite-a.scores.composite);
fs.writeFileSync(DIR+"/scores.json", JSON.stringify(pool,null,1));
console.log("pool size (mcap>=2B):", pool.length, "| rounds so far:", rounds.length);
console.log("\nTOP 50 by composite:");
pool.slice(0,50).forEach((p,i)=>console.log(`${String(i+1).padStart(2)} ${p.ticker.padEnd(6)} comp=${String(p.scores.composite).padStart(6)} fPE=${p.fpe??"-"} PEG=${p.peg??"-"} EPSny=${p.epsNextY??"-"}% YTD=${p.ytd??"-"}% 1Y=${p.yr??"-"}% mcap=$${p.mcap_b}B`));

// coiled-spring value list (contrarian): YTD<0, fPE<16, P/FCF<20
const springs = pool.filter(p=>p.ytd!==null&&p.ytd<0&&p.fpe!==null&&p.fpe<16&&p.pfcf!==null&&p.pfcf<20).sort((a,b)=>a.fpe-b.fpe);
console.log("\nCOILED-SPRING VALUE (YTD<0 & fPE<16 & P/FCF<20):", springs.length);
springs.slice(0,30).forEach(p=>console.log(`  ${p.ticker.padEnd(6)} fPE=${p.fpe} P/FCF=${p.pfcf} EPSny=${p.epsNextY??"-"}% YTD=${p.ytd}% 1Y=${p.yr}% mcap=$${p.mcap_b}B`));
fs.writeFileSync(DIR+"/rounds.jsonl", rounds.map(r=>JSON.stringify(r)).join("\n")+"\n");
