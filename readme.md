<br />
<div align="center">
  <a href="https://github.com/pnkr01/checktoxicity">
    <img src="https://img.freepik.com/free-vector/cute-bird-waving-hand-with-pilot-hat-cartoon-vector-icon-illustration-animal-nature-icon-isolated_138676-4688.jpg?size=626&ext=jpg&ga=GA1.2.1112508682.1676184457&semt=ais" alt="Logo" width="150" height="150">
  </a>

  <h1 align="center"><b>Check Toxicity</b></h1>
  <p align="center">
    "A script which detects toxicity and others wrong words"
    <br/>
  </p>
  <br />

<img src="https://img.shields.io/github/languages/code-size/pnkr01/checktoxicity?style=flat-square" alt="Code size" />
<img alt="GitHub contributors" src="https://img.shields.io/github/contributors/pnkr01/checktoxicity?style=flat-square">
<img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/pnkr01/checktoxicity?style=flat-square">
<img alt="GitHub Repo forks" src="https://img.shields.io/github/forks/pnkr01/checktoxicity?style=flat-square">
<img alt="GitHub Repo issues" src="https://img.shields.io/github/issues/pnkr01/checktoxicity?style=flat-square">


<br />
<a href="https://github.com/pnkr01/checktoxicity/">View Demo</a>
·
<a href="https://github.com/pnkr01/checktoxicity/issues">Report Bug</a>
·
<a href="https://github.com/pnkr01/checktoxicity/issues">Request Feature</a>
</div>


<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#tech-stacks">Tech Stacks</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
    </li>
    <li><a href="#app-screenshots">App ScreenShots</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

## About The Project
<p>This is PIP package is an API for hugging face <a href="https://huggingface.co/unitary/unbiased-toxic-roberta">Unbiased-toxic-toberta</a>
We can use it to detect toxicity in the sentence and can be used as a moderator.</p>
<p>To detect Toxicity and work as a moderation Layer.</p>
<div align="center">
<img alt="Check Toxicity Animation" src="https://img.freepik.com/free-vector/cute-bird-waving-hand-with-pilot-hat-cartoon-vector-icon-illustration-animal-nature-icon-isolated_138676-4688.jpg?size=1020&ext=jpg&ga=GA1.2.1112508682.1676184457&semt=ais">
</div>

### Tech Stacks

-Python


## Getting Started

You can test the crawling script in your own development environment. This section shows you how:

## Prerequisites
1. Open cmd type 'git clone https://github.com/pnkr01/checktoxicity'
2. cd checktoxicity
3. Create virtual environment run python3 -m pip install --user virtualenv
4. python3 -m venv venv
5. pip install requirements.txt
6. Now run 
7. Hurray! Code runs...
8. Detect Toxicity.


```python
from toxic.toxic import Toxic

r = Toxic("your query","your token ID")
print(r.getScoreFromAPI())
```

## APP Screenshots

<div align="center">
  <p float="left">
  <img src="https://github.com/pnkr01/checktoxicity/assets/83778936/8026c8a9-adb3-47c3-b638-c763166b4829" width="250"/>
  <img src="https://github.com/pnkr01/checktoxicity/assets/83778936/f81bc601-2457-4e2c-aa62-619613fce93f" width="250"/>               
</div>


