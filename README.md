# Rubik’s Clock
This repository provides a curated collection of resources on solving the [Rubik’s Clock](https://en.wikipedia.org/wiki/Rubik%27s_Clock), compiled by 2015HOUQ01 and 2017HEXI01.

## Table of Contents
1. Method I Use
2. 7-Simul
   - 2.1 7-Simul Flip
      - Bpaul’s Order 1 (x2 encoding)
      - Bpaul’s Order 2 (x2 encoding)
      - Tommy Cherry’s Order 1 (x2 encoding)
      - Tommy Cherry’s Order 2 (x2 encoding)
   - 2.2 7-Simul No-Flip
      - Bpaul’s Order (x2 encoding)
      - Bpaul’s Order (y2 encoding)
      - Tommy Cherry’s Order (x2 encoding)
      - Tommy Cherry’s Order (y2 encoding)
   - 2.3 7-Simul Trainers
3. Sheerin
4. Traditional Flip
5. God’s number

## 1. Method I Use
TODO

## 2. 7-Simul

### 2.1 7-Simul Flip

#### Bpaul’s Order 1 (x2 encoding)
| Pins | Simul-L                   | Simul-R                 |
|------|---------------------------|-------------------------|
| UL   | [UL] C → D                | [UR] **(-DR+R)+(-u+l)** |
| L    | [UL] C,D → R              | [UR] DR → R             |
| ur   | [UL] **(-R+D)+(-l+ul)**   | [UR] **(-u+c)**         |
| -x2- | --------M=(-U+C)--------- | ----------------------- |
| ur   | [UL] **(-r+d)+(-L+UL)**   | [UR] M                  |
| L    | [UL] D → R                | [UR] UR → DL            |
| UL   | [UL] UL,U,L,C → R,D       | [UR] DR → R,D           |
| \    | [UL] UL,U,L,C,R,D,DR → 12 | [UR] UR,DL → 12         |

#### Bpaul’s Order 2 (x2 encoding)
- [【いかのおすし(いかおす)】クロックの解法「7-simul flip(7sfndmw4lm)」の紹介](https://note.com/squid_sushi/n/nc1c62514b0f1)
- [【TetraWaffle】7 simul flip example solves/tutorials (4 versions)](https://www.youtube.com/watch?v=Hr87Qn9YljU)

| Pins | Simul-L                   | Simul-R         |
|------|---------------------------|-----------------|
| ur   | [UL] **(-R+D)+(-l+ul)**   | [UR] **(-u+c)** |
| L    | [UL] D → R                | [UR] **(-l+u)** |
| UL   | [UL] C → R,D              | [UR] DR → R,D   |
| -x2- | --------M=(-U+C)--------- | --------------- |
| ur   | [UL] **(-r+d)+(-L+UL)**   | [UR] M          |
| L    | [UL] D → R                | [UR] UR → DL    |
| UL   | [UL] UL,U,L,C → R,D       | [UR] DR → R,D   |
| \    | [UL] UL,U,L,C,R,D,DR → 12 | [UR] UR,DL → 12 |

#### Tommy Cherry’s Order 1 (x2 encoding)
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

#### Tommy Cherry’s Order 2 (x2 encoding)
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

### 2.2 7-Simul No-Flip

#### Bpaul’s Order (x2 encoding)
| Pins | Simul-L                   | Simul-R                 |
|------|---------------------------|-------------------------|
| dl   | [DL] **(-d+c)**           | [UR] **(-r+dr)+(-L+U)** |
| R    | [UL] **(-r+d)**           | [UR] U → L              |
| DR   | [UL] UL → U,L             | [DR] C → U,L            |
| ur   | [UL] **(-R+D)+(-l+ul)**   | [UR] **(-u+c)**         |
| L    | [UL] D → R                | [UR] UR → DL            |
| UL   | [UL] UL,U,L,C → R,D       | [UR] DR → R,D           |
| \    | [UL] UL,U,L,C,R,D,DR → 12 | [UR] UR,DL → 12         |

#### Bpaul’s Order (y2 encoding)
- [【Kiwi Cuber】Beginner 7 Simul Tutorial [EASY] - Advanced No-Flip Clock Method (bpaul)](https://www.youtube.com/watch?v=HGlJo6yqUkc)

| Pins | Simul-L                   | Simul-R                 |
|------|---------------------------|-------------------------|
| dl   | [DL] **(-u+c)**           | [UR] **(-l+ul)+(-L+U)** |
| R    | [UL] **(-l+u)**           | [UR] U → L              |
| DR   | [UL] UL → U,L             | [DR] C → U,L            |
| ur   | [UL] **(-R+D)+(-r+dr)**   | [UR] **(-d+c)**         |
| L    | [UL] D → R                | [UR] UR → DL            |
| UL   | [UL] UL,U,L,C → R,D       | [UR] DR → R,D           |
| \    | [UL] UL,U,L,C,R,D,DR → 12 | [UR] UR,DL → 12         |

#### Tommy Cherry’s Order (x2 encoding)
- [【Caleb Trelford】7 Simul Intermediate Clock Method Tutorial!](https://www.youtube.com/watch?v=MutprsOAhR4)
- [【Sukant】the 7simul video](https://www.youtube.com/watch?v=Lqv4HLZ22TQ)
- [【Tommy Cherry】7 Simul Tutorial (Clock) by Tommy Cherry](https://www.youtube.com/watch?v=ZX5ssGWUGb4)

| Pins | Simul-L                              | Simul-R                           |
|------|--------------------------------------|-----------------------------------|
| dl   | [DL] **(-d+c)**                      | [UR] **(-r+dr)+(-L+U)**           |
| R    | [UL] **(-r+d)**                      | [UR] U → L                        |
| DR   | [UL] UL → U,L                        | [DR] C → U,L                      |
| \    | [UL] **-[(-C+U)+D+(-l+ul)+(-r+dr)]** | [UR] **(-c+u)+d+(-L+UL)+(-R+DR)** |
| UL   | [UL] UL,U,L,C → D                    | [UR] DL → D                       |
| L    | [UL] UL,U,L,C,DL,D → R               | [UR] DR → R                       |
| ur   | [UL] UL,U,L,C,R,DL,D,DR → 12         | [UR] UR → 12                      |

#### Tommy Cherry’s Order (y2 encoding)
| Pins | Simul-L                              | Simul-R                           |
|------|--------------------------------------|-----------------------------------|
| dl   | [DL] **(-u+c)**                      | [UR] **(-l+ul)+(-L+U)**           |
| R    | [UL] **(-l+u)**                      | [UR] U → L                        |
| DR   | [UL] UL → U,L                        | [DR] C → U,L                      |
| \    | [UL] **-[(-C+U)+D+(-l+ul)+(-r+dr)]** | [UR] **(-c+u)+d+(-L+UL)+(-R+DR)** |
| UL   | [UL] UL,U,L,C → D                    | [UR] DL → D                       |
| L    | [UL] UL,U,L,C,DL,D → R               | [UR] DR → R                       |
| ur   | [UL] UL,U,L,C,R,DL,D,DR → 12         | [UR] UR → 12                      |

### 2.3 7-Simul Trainers
- [https://joshm2.github.io/7-Simul/](https://joshm2.github.io/7-Simul/)
- [https://sanya.sweetduet.info/cube/7simul_trainer/](https://sanya.sweetduet.info/cube/7simul_trainer/)

## 3. Sheerin
- [【Caleb Trelford】Learn How to Solve a Clock No-Flip in 10 Minutes (Beginner Tutorial) - Sheerin Method](https://www.youtube.com/watch?v=bHuuXDr_oYQ)

## 4. Traditional Flip
- [【2015HOUQ01】魔表技巧总结](https://tieba.baidu.com/p/4879288889)

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

## 5. God’s number
- [Rubik's Clock has now been solved!](https://www.cube20.org/clock/)
