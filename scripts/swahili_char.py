supported = """
mbwa
mbwe
mbwi 
ndwa
ndwe
ndwi
ngwa
ngwe
ngwi
njwa
njwe
njwi
nywa
nywe
shwa
shwe
shwi
chwa
chwe
chwi
pwa
pwe
pwi
pwo
swa
swe
swi
twa
twe
twi
zwa
zwe
zwi
cha
che
chi
cho
chu
dha
dhe
dhi
dho
dhu
gha
ghe
ghi
gho
ghu
kha
khe
kho
khu
mba
mbe
mbi
mbo
mbu
nda
nde
ndi
ndo
ndu
nga
nge
ngi
ngo
ngu
ng’a
ng’e
ng’o
nja
nje
nji
njo
nju
nya
nye
nyi
nyo
nyu
sha
she
shi
sho
shu
tha
the
thi
tho
thu
vya
vye
vyo
bwa
bwe
bwi
gwa
gwe
gwi
jwa
jwe
jwi
kwa 
kwe
kwi
lwa
lwe
lwi
mwa
mwe
mwi
nza
nze
nzi
nzo
nzu
ba
be
bi
bo
bu
da
de
di
do
du
fa
fe
fi
fo
fu
ga
ge
gi
go
gu
ha
he
hi
ho
hu
ja
je
ji
jo
ju
ka
ke
ki
ko
ku
la
le
li
lo
lu
ma
me
mi
mo
mu
na
ne
ni
no
nu
pa
pe
pi
po
pu
ra
re
ri
ro
ru
sa
se
si
so
su
ta
te
ti
to
tu
va
ve
vi
vo
vu
wa
we
wi
wo
wu
ya
ye
yi
yo
yu
vu
za
ze
zi
zo
zu
a
e
i
o
u
b
N
d
f
k
m
n
s
t
y
v
z
r
h
w
c
g
j
q
x
l
p
<
>
U
K
?
!
.
,
1
2
3
4
5
6
7
8
9
0
-

""
_

""".split()

char_map = {}
char_map[""] = 0
char_map["<SPACE>"] = 1
index = 2
for c in supported:
    char_map[c] = index
    index += 1
index_map = {v+1: k for k, v in char_map.items()}