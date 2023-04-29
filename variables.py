colors = {
        'board_color': (133,100,55),
        'corners': (66,30,6),
        'dark_corners': (42,19,4),
        'whi': (255,255,255),
        'bla': (0,0,0),
}
size = (1400,900)
k = (size[1]/18) # výška / 18
l = (size[0]/35) # šířka / 35
m = (size[0]/560) # šířka / 560
x = (38*m) # vzdálenost mezi dvěma sousedními středovými vrcholy trojúhelníků
gap = ((x*2)-10) # vzdálenost vždy mezi dvěma trojúhelníky na stejné pozici ale na druhé straně baru
a = (0.5*l) # základní souřadnice šířky pravého vrcholu trojúhelníků
b = (40*m) # základní souřadnice šířky levého vrcholu trojůhelníků
c = (25*m) # základní souřadnice šířky středového vrcholu trojúhelníků