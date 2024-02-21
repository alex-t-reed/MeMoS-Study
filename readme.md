# MeMoS Study (Memory, Money, & Self)

Welcome to the MeMoS Study repository! This repository contains materials and documentation related to the MeMoS Study, which investigates the impact of intrinsic and extrinsic motivation on decision strategies in memory-based tasks.

## About the Study

The MeMoS Study aims to determine whether intrinsically or extrinsically directed behavior may impact decision strategies for a memory-based task. The study compares behavior between four performance-based recognition memory tasks: baseline, "do better," memory-focused, and money-focused. This task is adapted by Alex Reed from the classic criterion shifting task by Sara Leslie in 2023, Sara Leslie, Courtney Durdle, and Alex Reed planned the MeMoS Study design. The MeMoS Study is currently in the process of data collection in the [Miller Memory Lab](https://labs.psych.ucsb.edu/miller/michael/) at UC Santa Barbara (UCSB) and is supported by a $750 UCSB Undergraduate Research & Creative Activites [(URCA) grant](https://urca.ucsb.edu/urca-grant/overview) procured by Alex Reed.

## Repository Structure

The repository is structured into four main sections, each dedicated to one of the task conditions:

- `memos-study-baseline/`: Materials and documentation related to the baseline task condition.
- `memos-study-do-better/`: Materials and documentation related to the "do better" task condition.
- `memos-study-memory/`: Materials and documentation related to the memory-focused task condition.
- `memos-study-money/`: Materials and documentation related to the money-focused task condition.

Within each folder, you will find specific materials such as code, data, documentation, and analysis scripts relevant to the corresponding task condition.

## Experiment Order

The study follows a specific order of tasks:

1. Baseline Task
2. Do Better Task
3. Memory Task or Money Task
4. Money Task or Memory Task

In each task, participants can earn up to $5, except $5 in the second task if they earned $5 in the first task. This adjustment is based on their improvement from the baseline task performance.

## Task Instructions Update

As of 2/20/24, the method for entering scores manually for the "do better" task has been updated. Instead of using the 'm' key, participants will now enter their baseline score in a designated section of the experiment prompt. This change aims to streamline in-person facilitation.

<img src="https://github.com/alex-t-reed/MeMoS-Study/blob/main/MeMoS_Do_Better_Prompt.png" width="300" alt="Image of Code Routine">

## How to Use

To run the experiments, you must download [PsychoPy](https://www.psychopy.org/download.html) (version 2021.2.3). Each experiment can be commenced with the green play button near the top of the experiment. Then you will be prompted to enter participant info such as ID and session, then hit OK and the experiment will begin. See below for example in the Baseline task:

<img src="https://github.com/alex-t-reed/MeMoS-Study/blob/main/MeMoS_Baseline_Taskbar.png" width="600" alt="Image of Baseline Taskbar">

Each `.psyexp` experiment file in the respective folders includes a code block allowing you to switch between actual and testing mode. Testing mode enables debugging without viewing all stimuli, facilitating quicker bug fixes and feature additions.

<img src="https://github.com/alex-t-reed/MeMoS-Study/blob/main/Code_Routine.png" width="300" alt="Image of Code Routine">

## Video Compression

Due to GitHub's 100 MB limit, videos in the repository have been heavily compressed using [FFmpeg](https://ffmpeg.org/) via the terminal and [FreeConvert](https://www.freeconvert.com/video-compressor/) for larger videos. Original experiment instructional videos are not included in this repository.

- Baseline Task video: 416.9 MB to 67.6 MB (FFmpeg and FreeConvert)
- Do Better Task video: 116.7 MB to 34.4 MB (FFmpeg)
- Memory Task video: 362.8 MB to 73.8 MB (FFmpeg and FreeConvert)
- Money Task video: 361.5 MB to 70.8 MB (FFmpeg and FreeConvert)

## Contributors

- [Alex Reed](https://www.linkedin.com/in/alextreed/): Research Assistant, Miller Memory Lab, UCSB, Senior Biopsychology Major (Developer of MeMoS Study code)
- [Sara Leslie](mailto:sara.leslie@psych.ucsb.edu): Original Task Developer & MeMoS Study Planner, Graduate Student in the Miller Memory Lab
- [Courtney Durdle](mailto:courtney.durdle@psych.ucsb.edu): MeMoS Study Planner, Graduate Student in the Miller Memory Lab

## Contact

For inquiries about the MeMoS Study or this repository, please contact:

- Alex Reed: [alexreed.atr@gmail.com](mailto:alexreed.atr@gmail.com)
- Sara Leslie: [sara.leslie@psych.ucsb.edu](mailto:sara.leslie@psych.ucsb.edu)
- Courtney Durdle: [courtney.durdle@psych.ucsb.edu](mailto:courtney.durdle@psych.ucsb.edu)

For more information about the Miller Memory Lab, please visit [https://labs.psych.ucsb.edu/miller/michael/](https://labs.psych.ucsb.edu/miller/michael/).

## Disclaimer

The materials and documentation provided in this repository are intended solely for academic and research purposes associated with the MeMoS Study (Memory, Money, & Self). Any utilization of these materials for the dissemination of study outcomes or for any purpose including academic and research endeavors is expressly prohibited, unless used solely for the purpose of replicating study procedures and results subsequent to the public disclosure of findings by the Miller Memory Lab. Additionally, explicit written authorization must be obtained from all contributors listed below before any such use.

Except in cases of preemptive publication to the Miller Memory Lab, individuals are granted permission to clone this repository, run the experiment, make alterations, and share the resulting modifications.

For inquiries regarding the utilization of these materials or the procurement of permission for publishing study outcomes, please contact:

- Alex Reed: [alexreed.atr@gmail.com](mailto:alexreed.atr@gmail.com)
- Sara Leslie: [sara.leslie@psych.ucsb.edu](mailto:sara.leslie@psych.ucsb.edu)
- Courtney Durdle: [courtney.durdle@psych.ucsb.edu](mailto:courtney.durdle@psych.ucsb.edu)
