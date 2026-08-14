#!/usr/bin/env python
"""Decide the #2 slot: INTU vs CRM, judged strictly on the 50%+ mandate."""
from decimal import Decimal as D, getcontext

getcontext().prec = 12

C = {
    'INTU': dict(px=D('325.25'), eps=D('16.76'), pe=D('19.4'), g=D('14.8'),
                 bb=D('3.1'), bear=D('-41.4'), rfcf=D('4.5'), shr3=D('-0.4'),
                 sbc=D('10.5'), ins=D('2.35'), days=17, off=D('-56.7'),
                 p5=D('1.6'), om=D('47.0')),
    'CRM': dict(px=D('192.74'), eps=D('9.80'), pe=D('19.7'), g=D('9.8'),
                bb=D('8.0'), bear=D('-37.9'), rfcf=D('6.7'), shr3=D('-4.1'),
                sbc=D('8.5'), ins=D('2.99'), days=18, off=D('-28.4'),
                p5=D('0.0'), om=D('21.8')),
}


def main():
    print('=' * 72)
    print('#2 SLOT: INTU vs CRM on the 50%+ mandate')
    print('=' * 72)

    for tk, c in C.items():
        eps2 = c['eps'] * (1 + c['g'] / 100) ** 2
        red = 1 - (1 - c['bb'] / 100) ** 2
        eps2a = eps2 / (1 - red)
        flat = eps2a * c['pe']
        up_flat = (flat / c['px'] - 1) * 100
        pe_need = (c['px'] * D('1.5')) / eps2a
        rerate = (pe_need / c['pe'] - 1) * 100
        odds = D(50) / abs(c['bear'])

        print()
        print('--- %s  ($%.2f) ---' % (tk, c['px']))
        print('  2yr EPS incl buyback      : %.2f  (EPS CAGR %.1f%%, shares -%.1f%%)'
              % (eps2a, c['g'], red * 100))
        print('  @ flat PE %.1fx            : $%.2f = %+.1f%%'
              % (c['pe'], flat, up_flat))
        print('  PE needed for +50%%         : %.1fx  (re-rate %+.1f%%)'
              % (pe_need, rerate))
        print('  bear downside             : %.1f%%   odds %.2fx'
              % (c['bear'], odds))
        print('  real FCF yield (ex-SBC)   : %.1f%%' % c['rfcf'])
        print('  3yr share change          : %.1f%%' % c['shr3'])
        print('  SBC / revenue             : %.1f%%' % c['sbc'])
        print('  insider ownership         : %.2f%%' % c['ins'])
        print('  5yr PE percentile         : %.1f%%' % c['p5'])
        print('  operating margin          : %.1f%%' % c['om'])
        print('  days to next earnings     : %d' % c['days'])

    print()
    print('=' * 72)
    print('VERDICT')
    print('=' * 72)
    print('INTU : better business (47%% op margin), deeper drawdown (-56.7%%),')
    print('       faster growth - but buyback cannot compound EPS (-0.4%% shares)')
    print('       and bear case is the worst of the four (-41.4%%).')
    print('CRM  : buyback actually shrinks shares (-4.1%%), higher real FCF')
    print('       yield (6.7%% vs 4.5%%), better odds, highest insider stake,')
    print('       and sits at its outright 5yr PE low (0.0 percentile).')


if __name__ == '__main__':
    main()
