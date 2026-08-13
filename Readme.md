<div align="center">

# Sahilpreet Singh

[![Typing SVG](https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=500&size=18&duration=3500&pause=1200&color=58A6FF&center=true&vCenter=true&width=600&lines=how+does+this+actually+work%3F;idea+%E2%86%92+model+%E2%86%92+code+%E2%86%92+experiment+%E2%86%92+analysis;simulation+%2B+physics+%2B+AI+%2B+hardware)](https://git.io/typing-svg)

`student` · `self-taught` · `Punjab, India`

</div>

<br>

## Earn from what I know, build from what I earn.

I'm a student teaching myself software engineering, electronics, simulation, mathematics, physics, and AI/ML — not to collect certificates, but because I want to be able to take a hard technical idea and turn it into something that actually runs.

I don't learn a tool because it's popular. I learn it because I want to know what's happening underneath it. If I use a library, a model, or an algorithm, at some point I go looking for the math or the mechanism behind it.

This profile isn't a finished product. It's a running log of that process.

<br>

## How I work

```
idea → model → code → experiment → data → visualization → analysis → improvement
```

I like simulations specifically because they let me run a system through thousands of conditions instead of trusting one deterministic answer. A lot of what's below is some version of: build the physics, run it many times, look at what the data says, make it better.

I version projects instead of abandoning them. A repo starting as "basic simulation" becoming "improved physics" becoming "optimization pass" is more honest than pretending v1 was the final version. Some of what's here is a finished engineering project, some of it is an open experiment, and some of it is just me learning something hard in public.

<br>

## Currently building

**JARVIS** — a goal-based computer-use agent for Windows, running entirely in the terminal. The constraint I set for myself: no hardcoded macros. It has to learn an application's interface while it's working the task, and verify outcomes rather than assume a clicked button did what it was supposed to do. Still early — the interesting part so far is the intent-over-commands design, not the coverage.

Alongside that, I'm pushing the Earth–Moon trajectory work from a single deterministic run toward an actual optimization problem — searching across trials for trajectories that trade off fuel usage, transfer time, and lunar orbital insertion, instead of me picking one by hand.

<br>

## Projects

**[Earth–Moon Orbital](https://github.com/Sahilpreetsinghvirdi/Earth-Moon-Orbital)**
Started as a 2D rocket trajectory simulation using Monte Carlo trials — randomizing launch parameters across thousands of runs instead of relying on one nominal trajectory — with numerical orbital dynamics, atmospheric drag, and lunar gravity, plotted live rather than dumped as static numbers. Current direction is turning trajectory selection into a search/optimization problem across fuel efficiency, transfer smoothness, and safe return.
`MATLAB` `Monte Carlo` `Orbital Mechanics` `Optimization`

**[AI NPC Simulation](https://github.com/Sahilpreetsinghvirdi/AI-NPC-simulation-with-finite-state-machine-architecture)**
A C++20 environment for exploring learned agent behavior — PPO, actor-critic, GAE, trajectory buffers, minibatch training, checkpointing for persistent learning across runs. I kept a traditional FSM baseline on purpose, so the system has a stable fallback instead of every behavior depending on a policy that's still training.
`C++20` `Reinforcement Learning` `PPO` `Finite State Machines`

**[Black Hole — MATLAB](https://github.com/Sahilpreetsinghvirdi/Black-hole-Matlab)**
Numerical modeling and visualization around black hole physics — an excuse to get comfortable with the kind of math that shows up later in orbital mechanics and dynamics.
`MATLAB` `Numerical Methods` `Physics`

**[4WD Autonomous Car](https://github.com/Sahilpreetsinghvirdi/4WD-Automatic-Car)**
Sensor-driven navigation on real hardware — the point where a simulation stops being forgiving. Ultrasonic sensing, motor control, obstacle avoidance logic, and all the ways physical systems don't behave like the model.
`Arduino` `Embedded Systems` `Robotics`

**[Stock Exchange](https://github.com/Sahilpreetsinghvirdi/Stock-Exchange)**
A full-stack virtual market — real-time simulation, portfolio tracking, trading logic, and a leaderboard. Less about finance, more about building a live system with state that has to stay consistent under concurrent activity.
`JavaScript` `Full-Stack` `Real-Time Systems`

<br>

## What I'm trying to understand

**Simulation & aerospace** — orbital mechanics, trajectory optimization, numerical methods for systems that don't have clean closed-form solutions.

**AI/ML** — not API calls. The math underneath: how optimization actually shapes a neural network, how reinforcement learning agents learn behavior instead of being handed it, what's really going on when people talk about scaling or alternative architectures.

**Physics & mathematics** — moving from school-level material toward the calculus, dynamics, and probability that simulation and AI actually run on.

**Hardware & embedded systems** — because a system that only exists in software hasn't been tested against reality yet.

I don't see these as separate subjects. Most of the interesting problems live at the point where two of them meet — a model that has to run in real time, a learned policy that has to control a physical motor, a trajectory that has to survive real drag and real gravity.

<br>

## Stack

`C++20` `C` `Python` `MATLAB` — core languages
`CMake` `Git` — build & version control
`Arduino` `ESP32` `KiCad` — embedded & hardware
`SolidWorks` — CAD & mechanical design
`Node.js` `React` — when a project needs a live interface

<br>

## Currently

<div align="center">

<img height="165" src="https://github-readme-stats.vercel.app/api?username=Sahilpreetsinghvirdi&show_icons=true&theme=tokyonight&hide_border=true&bg_color=0D1117&title_color=58A6FF&icon_color=58A6FF&text_color=C9D1D9" />
<img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=Sahilpreetsinghvirdi&layout=compact&theme=tokyonight&hide_border=true&bg_color=0D1117&title_color=58A6FF&text_color=C9D1D9" />

</div>

<br>

## Where this is going

Right now the throughline is: model something in math, simulate it, build the software around it, then see if it survives contact with real hardware or real-time constraints. Long term, that's the kind of engineer I want to be — someone who can move a hard idea from a differential equation to a working system, not someone who stops at the tutorial.

This is a journey, not a finished profile. Come back later — it should look different.

<div align="center">

---

`STATUS: BUILDING`

</div>
