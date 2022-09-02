# Autoclip

A util to clip according to call danmu. 

---

# How to use

1. Install Python, FFmpeg, and add them to path

2. Download this repository to your local storage

3. In command prompt, run `python main.py <your_rec_file>`

4. Wait for its output next to your rec file

---

# Directories and Files

+ sample\

  + analysis.xml: introduction to xml file format. 
  
  + test.xml: a sample test file that is used in the initial development. 
  
+ log.py: script for log output. Level of output can be changed by modifying `logLevel`. 

+ main.py: main file. 

+ vidproc.py: use FFmpeg to process video. 

+ xmlproc.py: xml file process. 

---

# Dependencies

The numbers following each term is the version used during development

+ [Python](https://www.python.org/) (3.9.10)

+ [FFmpeg](https://ffmpeg.org/) (4.2.2)

Newer versions should work properly but not tested. 

---

# References

+ 黑月流苏. https://zhidao.baidu.com/question/1430448163912263499.html

+ K-bai. https://github.com/K-bai/meumy-live-showcase/blob/master/server/danmu_analyse.py
