# Rubik’s Clock
This repository provides a curated collection of resources on solving the [Rubik’s Clock](https://en.wikipedia.org/wiki/Rubik%27s_Clock), compiled by [Qiyu Hou (2015HOUQ01)](https://cubing.com/results/person/2015HOUQ01) and [Xinan He (2017HEXI01)](https://cubing.com/results/person/2017HEXI01).

## Table of Contents
1. No-Flip
   - 1.1 7-Simul (7S)
     - 1.1.1 Tommy Cherry’s Order (T7S)
       - T7S x2 encoding
       - T7S y2 encoding
     - 1.1.2 Bpaul’s Order (B7S)
       - B7S x2 encoding
       - B7S y2 encoding
     - 1.1.3 Limited
       - 6-Simul Tilt
       - Pseudo 6-Simul
   - 1.2 Other
     - 1.2.1 Sheerin
     - 1.2.2 Four Halves
     - 1.2.3 Yunhao Lou’s Method
2. Flip
   - 2.1 7-Simul x2 Flip (7SF)
     - 2.1.1 Tommy Cherry’s Order (T7SF)
       - T7SF Order 1
       - T7SF Order 2
     - 2.1.2 Bpaul’s Order (B7SF)
       - B7SF Order 1
       - B7SF Order 2
   - 2.2 Other
3. God’s number
4. Simulators / Trainers

## 1. No-Flip

### 1.1 7-Simul (7S)

#### 1.1.1 Tommy Cherry’s Order (T7S)

##### T7S x2 encoding
- [【Tommy Cherry】7 Simul Tutorial (Clock) by Tommy Cherry](https://www.youtube.com/watch?v=ZX5ssGWUGb4)
- [【Sukant】the 7simul video](https://www.youtube.com/watch?v=Lqv4HLZ22TQ)
- [【Caleb Trelford】7 Simul Intermediate Clock Method Tutorial!](https://www.youtube.com/watch?v=MutprsOAhR4)

| Pins | Simul-L                                                              | Simul-R                           |
|------|----------------------------------------------------------------------|-----------------------------------|
| dl   | [DL] **(-d+c)**                                                      | [UR] **(-r+dr)+(-L+U)**           |
| R    | [UL] **(-r+d)**                                                      | [UR] U → L                        |
| DR   | [UL] UL → U,L                                                        | [DR] C → U,L                      |
| \    | [UL] **(-U+UR)+(-D+C)+(-ul+l)+r** OR **-[(-C+U)+D+(-l+ul)+(-r+dr)]** | [UR] **(-c+u)+d+(-L+UL)+(-R+DR)** |
| UL   | [UL] UL,U,L,C → D                                                    | [UR] DL → D                       |
| L    | [UL] UL,U,L,C,DL,D → R                                               | [UR] DR → R                       |
| ur   | [UL] UL,U,L,C,R,DL,D,DR → 12                                         | [UR] UR → 12                      |

##### T7S y2 encoding
| Pins | Simul-L                              | Simul-R                           |
|------|--------------------------------------|-----------------------------------|
| dl   | [DL] **(-u+c)**                      | [UR] **(-l+ul)+(-L+U)**           |
| R    | [UL] **(-l+u)**                      | [UR] U → L                        |
| DR   | [UL] UL → U,L                        | [DR] C → U,L                      |
| \    | [UL] **-[(-C+U)+D+(-l+ul)+(-r+dr)]** | [UR] **(-c+u)+d+(-L+UL)+(-R+DR)** |
| UL   | [UL] UL,U,L,C → D                    | [UR] DL → D                       |
| L    | [UL] UL,U,L,C,DL,D → R               | [UR] DR → R                       |
| ur   | [UL] UL,U,L,C,R,DL,D,DR → 12         | [UR] UR → 12                      |

#### 1.1.2 Bpaul’s Order (B7S)

##### B7S x2 encoding
| Pins | Simul-L                   | Simul-R                 |
|------|---------------------------|-------------------------|
| dl   | [DL] **(-d+c)**           | [UR] **(-r+dr)+(-L+U)** |
| R    | [UL] **(-r+d)**           | [UR] U → L              |
| DR   | [UL] UL → U,L             | [DR] C → U,L            |
| ur   | [UL] **(-R+D)+(-l+ul)**   | [UR] **(-u+c)**         |
| L    | [UL] D → R                | [UR] **(-l+u)**         |
| UL   | [UL] UL,U,L,C → R,D       | [UR] DR → R,D           |
| \    | [UL] UL,U,L,C,R,D,DR → 12 | [UR] UR,DL → 12         |

##### B7S y2 encoding
- [【Kiwi Cuber】Beginner 7 Simul Tutorial [EASY] - Advanced No-Flip Clock Method (bpaul)](https://www.youtube.com/watch?v=HGlJo6yqUkc)

| Pins | Simul-L                   | Simul-R                 |
|------|---------------------------|-------------------------|
| dl   | [DL] **(-u+c)**           | [UR] **(-l+ul)+(-L+U)** |
| R    | [UL] **(-l+u)**           | [UR] U → L              |
| DR   | [UL] UL → U,L             | [DR] C → U,L            |
| ur   | [UL] **(-R+D)+(-r+dr)**   | [UR] **(-d+c)**         |
| L    | [UL] D → R                | [UR] **(-r+d)**         |
| UL   | [UL] UL,U,L,C → R,D       | [UR] DR → R,D           |
| \    | [UL] UL,U,L,C,R,D,DR → 12 | [UR] UR,DL → 12         |

#### 1.1.3 Limited

##### 6-Simul Tilt
[【TetraWaffle】Right and Left tilt 6 simult pinsets | Advanced 7 simul tutorial (Updated version)](https://www.youtube.com/watch?v=v82-CfcN3zM)

##### Pseudo 6-Simul
[【TetraWaffle】Intro - What is Pseudo 6 Simul? Updated P6s Tutorial | Part 0](https://www.youtube.com/watch?v=pQnbSJg4fCU)
[【TetraWaffle】Slashless 1 - Updated Pseudo 6 Simul Tutorial | Part 1](https://www.youtube.com/watch?v=Y365Dna8DAk)
[【TetraWaffle】L and Fall - Updated Pseudo 6 Simul Tutorial | Part 2](https://www.youtube.com/watch?v=1l-2u8zfWXE)

### 1.2 Other

#### 1.2.1 Sheerin
- [【Caleb Trelford】Learn How to Solve a Clock No-Flip in 10 Minutes (Beginner Tutorial) - Sheerin Method](https://www.youtube.com/watch?v=bHuuXDr_oYQ)

#### 1.2.2 Four Halves
- [【Jupilogy】Four halves | no-flip clock method](https://www.youtube.com/watch?v=6Cc1a5ExwyQ)

#### 1.2.3 Yunhao Lou’s Method
- [【Yunhao Lou】Clock No-Flip ao5=4.46 + Tutorial in description](https://www.youtube.com/watch?v=Ue0NqRdt44o)
- [【Diwiqxaxesret】魔表：同时操作两面十字的不翻面还原](https://www.bilibili.com/opus/552232047219156839)

## 2. Flip

### 2.1 7-Simul x2 Flip (7SF)

#### 2.1.1 Tommy Cherry’s Order (T7SF)

##### T7SF Order 1
- [【JJ Cuber】Tommy V2 - Advanced 7-Simul Flip Tutorial (Clock)](https://www.youtube.com/watch?v=A1iUwpWzyXw)

| Pins | Simul-L                              | Simul-R                           |
|------|--------------------------------------|-----------------------------------|
| UL   | [UL] C → D                           | [UR] **(-DR+R)+(-u+l)**           |
| L    | [UL] C,D → R                         | [UR] DR → R                       |
| ur   | [UL] **(-R+D)+(-l+ul)**              | [UR] **(-u+c)**                   |
| -x2- | ------------------------------------ | --------------------------------- |
| \    | [UL] **-[(-c+u)+d+(-L+UL)+(-R+DR)]** | [UR] **(-C+U)+D+(-l+ul)+(-r+dr)** |
| UL   | [UL] UL,U,L,C → D                    | [UR] DL → D                       |
| L    | [UL] UL,U,L,C,DL,D → R               | [UR] DR → R                       |
| ur   | [UL] UL,U,L,C,R,DL,D,DR → 12         | [UR] UR → 12                      |

##### T7SF Order 2
| Pins | Simul-L                              | Simul-R                           |
|------|--------------------------------------|-----------------------------------|
| ur   | [UL] **(-R+D)+(-l+ul)**              | [UR] **(-u+c)**                   |
| L    | [UL] D → R                           | [UR] **(-l+u)**                   |
| UL   | [UL] C → R,D                         | [UR] DR → R,D                     |
| -x2- | ------------------------------------ | --------------------------------- |
| \    | [UL] **-[(-c+u)+d+(-L+UL)+(-R+DR)]** | [UR] **(-C+U)+D+(-l+ul)+(-r+dr)** |
| UL   | [UL] UL,U,L,C → D                    | [UR] DL → D                       |
| L    | [UL] UL,U,L,C,DL,D → R               | [UR] DR → R                       |
| ur   | [UL] UL,U,L,C,R,DL,D,DR → 12         | [UR] UR → 12                      |

#### 2.1.2 Bpaul’s Order (B7SF)

##### B7SF Order 1
| Pins | Simul-L                   | Simul-R                 |
|------|---------------------------|-------------------------|
| UL   | [UL] C → D                | [UR] **(-DR+R)+(-u+l)** |
| L    | [UL] C,D → R              | [UR] DR → R             |
| ur   | [UL] **(-R+D)+(-l+ul)**   | [UR] **(-u+c)**         |
| -x2- | ------------------------- | ----------------------- |
| ur   | [UL] **(-r+d)+(-L+UL)**   | [UR] **(-U+C)**         |
| L    | [UL] D → R                | [UR] **(-L+U)**         |
| UL   | [UL] UL,U,L,C → R,D       | [UR] DR → R,D           |
| \    | [UL] UL,U,L,C,R,D,DR → 12 | [UR] UR,DL → 12         |

##### B7SF Order 2
- [【いかのおすし(いかおす)】クロックの解法「7-simul flip(7sfndmw4lm)」の紹介](https://note.com/squid_sushi/n/nc1c62514b0f1)
- [【TetraWaffle】7 simul flip example solves/tutorials (4 versions)](https://www.youtube.com/watch?v=Hr87Qn9YljU)
- [【TheCubicle】Tommy Cherry Shows Tymon How to Solve Clock Using 7 Simul](https://www.youtube.com/watch?v=Biu9QV6c-FI)

| Pins | Simul-L                   | Simul-R         |
|------|---------------------------|-----------------|
| ur   | [UL] **(-R+D)+(-l+ul)**   | [UR] **(-u+c)** |
| L    | [UL] D → R                | [UR] **(-l+u)** |
| UL   | [UL] C → R,D              | [UR] DR → R,D   |
| -x2- | ------------------------- | --------------- |
| ur   | [UL] **(-r+d)+(-L+UL)**   | [UR] **(-U+C)** |
| L    | [UL] D → R                | [UR] **(-L+U)** |
| UL   | [UL] UL,U,L,C → R,D       | [UR] DR → R,D   |
| \    | [UL] UL,U,L,C,R,D,DR → 12 | [UR] UR,DL → 12 |

### 2.2 Other
- [【TetraWaffle】10 Move Memoless (10MM)](https://docs.google.com/document/d/1-6ljL2571EN3AxEap037aH3Xr_pxO85BPV9Fsrv4-rw)
- [【Diwiqxaxesret】魔表技巧教程：从入门到WR](https://www.bilibili.com/video/BV1Mv411p7KR)
- [【半杯奶霜】魔表教程](https://www.bilibili.com/video/BV1sx411L7RF)
- [【Qiyu Hou】2015HOUQ01-魔表技巧总结](https://tieba.baidu.com/p/4879288889)
- [【深色伏特加】魔表教程第二版](https://v.youku.com/video?vid=XOTU4NDM3OTA4)
- [【Jaap Scherphuis】Jaap's Puzzle Page](https://www.jaapsch.net/puzzles/clock.htm)
- [【Stefan Pochmann】Speedsolving Rubik's Clock](https://www.stefan-pochmann.info/spocc/speedsolving/clock/)

| Pins | Steps                           |
|------|---------------------------------|
| UR   | [UR] U → L                      |
| DR   | [DR] C → U,L                    |
| UL   | [UL] U,L,C → R                  |
| U    | [UR] U,L,C,R → D                |
| dr   | [UR] U,L,C,R,D → 12             |
| -x2- | ------------------------------- |
| UR   | [UR] U → L                      |
| DR   | [DR] C → U,L                    |
| UL   | [UL] U,L,C → R                  |
| U    | [UR] U,L,C,R → D                |
| dl   | [UR] U,L,C,R,D → DL             |
| dr   | [UL] U,L,C,R,DL,D → DR          |
| ul   | [UR] U,L,C,R,DL,D,DR → UL       |
| ur   | [UL] UL,U,L,C,R,DL,D,DR → UR    |
| ALL  | [UR] UL,U,UR,L,C,R,DL,D,DR → 12 |

## 3. God’s number
- [Rubik's Clock has now been solved!](https://www.cube20.org/clock/)

## 4. Simulators / Trainers
- [https://sanya.sweetduet.info/cube/7simul_trainer/](https://sanya.sweetduet.info/cube/7simul_trainer/)
- [https://joshm2.github.io/7-Simul/](https://joshm2.github.io/7-Simul/)
- [https://www.jaapsch.net/puzzles/javascript/clockj.htm](https://www.jaapsch.net/puzzles/javascript/clockj.htm)
- [https://www.kongregate.com/games/d4m4s74/rubiks-clock-simulator](https://www.kongregate.com/games/d4m4s74/rubiks-clock-simulator)
