#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on Tue Feb 20 01:55:56 2024
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

import psychopy
psychopy.useVersion('2021.2.3')


from psychopy import locale_setup
from psychopy import prefs
prefs.hardware['audioLib'] = 'ptb'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'memos_do_better_task'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/alexreed/Desktop/Coding/MeMoS-Study/memos-study-do-better/MeMoS_Do_Better_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1800, 1169], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Overall_Instruction"
Overall_InstructionClock = core.Clock()
Overall_Instruction_text = visual.TextStim(win=win, name='Overall_Instruction_text',
    text='WELCOME!\n\nIn this experiment, you will make decisions and rate your confidence. \n\nJust try your best, even if it feels difficult. \n\nPress the spacebar to continue.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=1.2, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Overall_Instruction_key = keyboard.Keyboard()

# Initialize components for Routine "Sound_Check"
Sound_CheckClock = core.Clock()
Overall_Instruction_text_2 = visual.TextStim(win=win, name='Overall_Instruction_text_2',
    text='Please ensure the volume is on and that you can hear this sound which will shortly play. ',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=1.2, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Overall_Instruction_key_2 = keyboard.Keyboard()
sound_1 = sound.Sound('B', secs=-1, stereo=True, hamming=True,
    name='sound_1')
sound_1.setVolume(0.5)
Continue = visual.TextStim(win=win, name='Continue',
    text='If you did not hear the sound increase the volume using the keyboard. Press the spacebar to continue.',
    font='Open Sans',
    pos=(0, -.3), height=0.05, wrapWidth=1.2, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "Now_The_Video_Will_Play"
Now_The_Video_Will_PlayClock = core.Clock()
Overall_Instruction_text_3 = visual.TextStim(win=win, name='Overall_Instruction_text_3',
    text='You will now be shown an instructional video about the task. You cannot pause or rewatch the video so pay close attention.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=1.2, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_22 = keyboard.Keyboard()
Continue_2 = visual.TextStim(win=win, name='Continue_2',
    text='Press the spacebar to continue.',
    font='Open Sans',
    pos=(0, -.3), height=0.05, wrapWidth=1.2, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "videoInstructions"
videoInstructionsClock = core.Clock()
movie = visual.MovieStim3(
    win=win, name='movie',
    noAudio = False,
    filename='resources/videos/MeMoS Experiment 2 Instructions - Do Better.mp4',
    ori=0.0, pos=(0, 0), opacity=None,
    loop=False,
    size=[1280,720],
    depth=0.0,
    )

# Initialize components for Routine "Commitment_Do_Better_Response"
Commitment_Do_Better_ResponseClock = core.Clock()
commitment_question = visual.TextStim(win=win, name='commitment_question',
    text='Write your commitment toward doing better on this task and your strategy toward doing better.',
    font='Open Sans',
    pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
commitment_question_response = visual.TextBox2(
     win, text='Please type your response here . . . ', font='Open Sans',
     pos=(0, 0),     letterHeight=0.02,
     size=(1.0, 0.09), borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=1.0,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0,
     anchor='center',
     fillColor='white', borderColor=None,
     flipHoriz=False, flipVert=False,
     editable=True,
     name='commitment_question_response',
     autoLog=True,
)
mouse_1 = event.Mouse(win=win)
x, y = [None, None]
mouse_1.mouseClock = core.Clock()
Clickable_1 = visual.TextStim(win=win, name='Clickable_1',
    text='When finished, click here to go to the next question. ',
    font='Open Sans',
    pos=(0.3, -0.3), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "Code"
CodeClock = core.Clock()
# Task by Sara Leslie, 2023
# Repurposed for MeMoS Study by Alex Reed, 2023

import random  # Import the random module

mode = 'actual'

if mode == 'testing':
    # Define necessary variables for testing block
    num_study = 3
    pics_per_block = 6
    old_per_cond = 1
    new_per_cond = 1
    num_test = old_per_cond + new_per_cond
    num_items = pics_per_block
    num_blocks = 2
elif mode == 'actual':
    # Define necessary variables for actual block
    num_study = 27
    pics_per_block = 54
    old_per_cond = 9
    new_per_cond = 9
    num_test = old_per_cond + new_per_cond
    num_items = pics_per_block
    num_blocks = 6

# Initialize variables
blockn = 0
blocknumber = 1
blocknumber_alt = 1
reward_number = 0
themecounter = 0
condorder_counter = 0
condorder_now = []
trialpay = 0
totaltrialnum = 1

# Define the permutations of conditions for the blocks
cond_perm = [[0, 1, 2], [1, 0, 2], [2, 0, 1],
             [0, 2, 1], [1, 2, 0], [2, 1, 0],
             [0, 1, 2], [1, 0, 2], [2, 0, 1],
             [0, 2, 1], [1, 2, 0], [2, 1, 0]]

# Shuffle the permutation list using the random module
random.shuffle(cond_perm)

# Define face sets for each category
faceset1 = ["resources/faceset7/faceset7_" + str(num) + ".jpg" for num in range(1, num_items + 1)]
faceset2 = ["resources/faceset8/faceset8_" + str(num) + ".jpg" for num in range(1, num_items + 1)]
faceset3 = ["resources/faceset9/faceset9_" + str(num) + ".jpg" for num in range(1, num_items + 1)]
faceset4 = ["resources/faceset10/faceset10_" + str(num) + ".jpg" for num in range(1, num_items + 1)]
faceset5 = ["resources/faceset11/faceset11_" + str(num) + ".jpg" for num in range(1, num_items + 1)]
faceset6 = ["resources/faceset12/faceset12_" + str(num) + ".jpg" for num in range(1, num_items + 1)]

# Shuffle each face set using the random module
random.shuffle(faceset1)
random.shuffle(faceset2)
random.shuffle(faceset3)
random.shuffle(faceset4)
random.shuffle(faceset5)
random.shuffle(faceset6)

# Organize the face sets in an image array
imagearray = [
    faceset1,
    faceset2,
    faceset3,
    faceset4,
    faceset5,
    faceset6
]

# Initialize components for Routine "OverallBlockCode"
OverallBlockCodeClock = core.Clock()

# Initialize components for Routine "ReminderMessage"
ReminderMessageClock = core.Clock()
studyreminder = visual.TextStim(win=win, name='studyreminder',
    text='Reminders: \n\nIf you need to take a break, it’s best to do so at the end of a decision phase.\n\nPlease do not use any aids for the memory part of the task.\n\nPlease try to accurately report your confidence. \n\nPress the spacebar to continue. ',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=1.2, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_15 = keyboard.Keyboard()

# Initialize components for Routine "StudyBlockMessage"
StudyBlockMessageClock = core.Clock()
studyblockinfo = visual.TextStim(win=win, name='studyblockinfo',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
s_key = visual.TextStim(win=win, name='s_key',
    text='Please press the ’s’ key to start this block. ',
    font='Open Sans',
    pos=(0, -.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_proceed = keyboard.Keyboard()

# Initialize components for Routine "Code_StudyBlock"
Code_StudyBlockClock = core.Clock()

# Initialize components for Routine "Learning_Trial"
Learning_TrialClock = core.Clock()
LearningImage = visual.ImageStim(
    win=win,
    name='LearningImage', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "Blank300"
Blank300Clock = core.Clock()
polygon = visual.ShapeStim(
    win=win, name='polygon', vertices='cross',
    size=(0.05025, 0.05025),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "studyloop"
studyloopClock = core.Clock()

# Initialize components for Routine "TestBlockCode"
TestBlockCodeClock = core.Clock()

# Initialize components for Routine "TestBlockMessage"
TestBlockMessageClock = core.Clock()
testblockreport = visual.TextStim(win=win, name='testblockreport',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
spacebar2 = visual.TextStim(win=win, name='spacebar2',
    text='Please press the space bar to continue. ',
    font='Open Sans',
    pos=(0, -.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_proceed2 = keyboard.Keyboard()

# Initialize components for Routine "CLNLoopCode"
CLNLoopCodeClock = core.Clock()

# Initialize components for Routine "TestBlock_Select"
TestBlock_SelectClock = core.Clock()

# Initialize components for Routine "Payoff_InfoScreen"
Payoff_InfoScreenClock = core.Clock()
text_correctpayoff = visual.TextStim(win=win, name='text_correctpayoff',
    text='*** PAY UPDATE ***\n',
    font='Open Sans',
    pos=(0, 0.25), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
payalert = visual.TextStim(win=win, name='payalert',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=1.2, ori=0.0, 
    color='cyan', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
press_p = visual.TextStim(win=win, name='press_p',
    text='Press the ‘p’ button to continue.',
    font='Open Sans',
    pos=(0, -.35), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_12 = keyboard.Keyboard()

# Initialize components for Routine "Code_TestBlock"
Code_TestBlockClock = core.Clock()

# Initialize components for Routine "TestTrial"
TestTrialClock = core.Clock()
Learning_TestTrial = visual.ImageStim(
    win=win,
    name='Learning_TestTrial', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.201, 0.256),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
OLD = visual.TextStim(win=win, name='OLD',
    text='j = OLD',
    font='Open Sans',
    pos=(-0.33, -0.28), height=0.045, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
NEW = visual.TextStim(win=win, name='NEW',
    text='',
    font='Open Sans',
    pos=(0.42, -0.28), height=0.045, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
Old_Points_minus = visual.TextStim(win=win, name='Old_Points_minus',
    text='',
    font='Open Sans',
    pos=(-.33, -0.34), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
Points_add_Old = visual.TextStim(win=win, name='Points_add_Old',
    text='',
    font='Open Sans',
    pos=(-.33, -0.40), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
New_Points_minus = visual.TextStim(win=win, name='New_Points_minus',
    text='',
    font='Open Sans',
    pos=(0.42, -0.34), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
Points_Add_New = visual.TextStim(win=win, name='Points_Add_New',
    text='+5  points correct',
    font='Open Sans',
    pos=(0.42, -0.40), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
TestTrialKey = keyboard.Keyboard()

# Initialize components for Routine "updatepay"
updatepayClock = core.Clock()

# Initialize components for Routine "ConfidenceRating"
ConfidenceRatingClock = core.Clock()
LT_Block_1_Confidence = visual.TextStim(win=win, name='LT_Block_1_Confidence',
    text='Please rate your confidence on whether your decision is accurate.\n\n  low   medium   high  \n\n   s      d        f  ',
    font='Open Sans',
    pos=(0, -0.1), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_confidence = keyboard.Keyboard()

# Initialize components for Routine "Running_Report"
Running_ReportClock = core.Clock()

# Initialize components for Routine "JustBlank"
JustBlankClock = core.Clock()
text_9 = visual.TextStim(win=win, name='text_9',
    text='\n',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "testloop"
testloopClock = core.Clock()

# Initialize components for Routine "Update_CLN"
Update_CLNClock = core.Clock()

# Initialize components for Routine "BlockReport"
BlockReportClock = core.Clock()
blockreportearn = visual.TextStim(win=win, name='blockreportearn',
    text='',
    font='Open Sans',
    pos=(0, .2), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
total_earning_report = visual.TextStim(win=win, name='total_earning_report',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
spacetocontinue = visual.TextStim(win=win, name='spacetocontinue',
    text='\nPress the space bar to continue',
    font='Open Sans',
    pos=(0, -.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_11 = keyboard.Keyboard()

# Initialize components for Routine "blockadvance"
blockadvanceClock = core.Clock()

# Initialize components for Routine "EndVariables"
EndVariablesClock = core.Clock()

# Initialize components for Routine "Blank100"
Blank100Clock = core.Clock()
Blank_2 = visual.TextStim(win=win, name='Blank_2',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "QuestionProb"
QuestionProbClock = core.Clock()
probq = visual.TextStim(win=win, name='probq',
    text='What percent of the faces do you think were actually OLD?',
    font='Open Sans',
    pos=(0, .4), height=0.04, wrapWidth=1.2, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
probold_slider = visual.Slider(win=win, name='probold_slider',
    startValue=0, size=(1.0, 0.03), pos=(0, 0), units=None,
    labels=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], ticks=(0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100), granularity=0.1,
    style='rating', styleTweaks=('triangleMarker',), opacity=None,
    color='LightGray', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.02,
    flip=False, depth=-1, readOnly=False)
mouse_probold = event.Mouse(win=win)
x, y = [None, None]
mouse_probold.mouseClock = core.Clock()
instructions = visual.TextStim(win=win, name='instructions',
    text='Using the mouse, click on the line above to give your answer. A red triangle should appear to indicate your choice. Then press the ‘c’ key to continue.',
    font='Open Sans',
    pos=(0, -.3), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
key_resp_16 = keyboard.Keyboard()

# Initialize components for Routine "QuestionCorrect"
QuestionCorrectClock = core.Clock()
correctq = visual.TextStim(win=win, name='correctq',
    text='What percent of your answers do you think were correct?',
    font='Open Sans',
    pos=(0, .4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
probcorrect_slider = visual.Slider(win=win, name='probcorrect_slider',
    startValue=0, size=(1.0, 0.03), pos=(0, 0), units=None,
    labels=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], ticks=(0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100), granularity=0.1,
    style='rating', styleTweaks=('triangleMarker',), opacity=None,
    color='LightGray', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.02,
    flip=False, depth=-1, readOnly=False)
mouse_probcorrect = event.Mouse(win=win)
x, y = [None, None]
mouse_probcorrect.mouseClock = core.Clock()
instructions_2 = visual.TextStim(win=win, name='instructions_2',
    text='Using the mouse, click on the line above to give your answer. A red triangle should appear to indicate your choice. Then press the ‘c’ key to continue.',
    font='Open Sans',
    pos=(0, -.3), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
key_resp_18 = keyboard.Keyboard()

# Initialize components for Routine "Question_SelfRank"
Question_SelfRankClock = core.Clock()
selfrankq = visual.TextStim(win=win, name='selfrankq',
    text='Suppose you are one of 100 randomly chosen people who completed this task. What number of those people would you expect to perform better than you?',
    font='Open Sans',
    pos=(0, .4), height=0.04, wrapWidth=1.2, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
selfrank_slider_s1 = visual.Slider(win=win, name='selfrank_slider_s1',
    startValue=0, size=(1.0, 0.03), pos=(0, 0), units=None,
    labels=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], ticks=(0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100), granularity=0.1,
    style='rating', styleTweaks=('triangleMarker',), opacity=None,
    color='LightGray', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.02,
    flip=False, depth=-1, readOnly=False)
mouse_selfrank = event.Mouse(win=win)
x, y = [None, None]
mouse_selfrank.mouseClock = core.Clock()
instructions_3 = visual.TextStim(win=win, name='instructions_3',
    text='Using the mouse, click on the line above to give your answer. A red triangle should appear to indicate your choice. Then press the ‘c’ key to continue.',
    font='Open Sans',
    pos=(0, -.3), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
key_resp_19 = keyboard.Keyboard()

# Initialize components for Routine "QuestionHighConf"
QuestionHighConfClock = core.Clock()
highconfq = visual.TextStim(win=win, name='highconfq',
    text='When you say HIGH confidence, what percent of the time are you correct?',
    font='Open Sans',
    pos=(0, .3), height=0.04, wrapWidth=1.2, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
highconf_slider = visual.Slider(win=win, name='highconf_slider',
    startValue=0, size=(1.0, 0.03), pos=(0, 0), units=None,
    labels=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], ticks=(0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100), granularity=0.1,
    style='rating', styleTweaks=('triangleMarker',), opacity=None,
    color='LightGray', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.02,
    flip=False, depth=-1, readOnly=False)
mouse_highconf = event.Mouse(win=win)
x, y = [None, None]
mouse_highconf.mouseClock = core.Clock()
instructions2 = visual.TextStim(win=win, name='instructions2',
    text='Using the mouse, click on the line above to give your answer. A red triangle should appear to indicate your choice. Then press the ‘c’ key to continue.',
    font='Open Sans',
    pos=(0, -.3), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
key_resp_17 = keyboard.Keyboard()

# Initialize components for Routine "QuestionLowConf"
QuestionLowConfClock = core.Clock()
lowconfq = visual.TextStim(win=win, name='lowconfq',
    text='When you say LOW confidence, what percent of the time are you correct?',
    font='Open Sans',
    pos=(0, .3), height=0.04, wrapWidth=1.2, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
lowconf_slider = visual.Slider(win=win, name='lowconf_slider',
    startValue=0, size=(1.0, 0.03), pos=(0, 0), units=None,
    labels=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], ticks=(0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100), granularity=0.1,
    style='rating', styleTweaks=('triangleMarker',), opacity=None,
    color='LightGray', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.02,
    flip=False, depth=-1, readOnly=False)
mouse_lowconf = event.Mouse(win=win)
x, y = [None, None]
mouse_lowconf.mouseClock = core.Clock()
instructions3 = visual.TextStim(win=win, name='instructions3',
    text='Using the mouse, click on the line above to give your answer. A red triangle should appear to indicate your choice. Then press the ‘c’ key to continue.',
    font='Open Sans',
    pos=(0, -.3), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
key_resp_14 = keyboard.Keyboard()

# Initialize components for Routine "QuestionMoneyScale"
QuestionMoneyScaleClock = core.Clock()
moneyscaleq1 = visual.TextStim(win=win, name='moneyscaleq1',
    text='Overall, rate to what extent you based your final decision on the money?',
    font='Open Sans',
    pos=(0, .3), height=0.04, wrapWidth=1.2, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
moneyscale_q1 = visual.Slider(win=win, name='moneyscale_q1',
    startValue=0, size=(1.0, 0.03), pos=(0, 0), units=None,
    labels=[1, 2, 3, 4, 5, 6], ticks=(1,2,3,4,5,6), granularity=0.1,
    style='rating', styleTweaks=('triangleMarker',), opacity=None,
    color='LightGray', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.02,
    flip=False, depth=-1, readOnly=False)
mouse_lowconf_2 = event.Mouse(win=win)
x, y = [None, None]
mouse_lowconf_2.mouseClock = core.Clock()
instructions3_2 = visual.TextStim(win=win, name='instructions3_2',
    text='Using the mouse, click on the line above to give your answer. A red triangle should appear to indicate your choice. Then press the ‘c’ key to continue.',
    font='Open Sans',
    pos=(0, -.3), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
key_resp_23 = keyboard.Keyboard()

# Initialize components for Routine "QuestionMemoryScale"
QuestionMemoryScaleClock = core.Clock()
memoryscaleq1 = visual.TextStim(win=win, name='memoryscaleq1',
    text='Overall, rate to what extent you based your final decision on your memory?',
    font='Open Sans',
    pos=(0, .3), height=0.04, wrapWidth=1.2, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
memoryscale_q1 = visual.Slider(win=win, name='memoryscale_q1',
    startValue=0, size=(1.0, 0.03), pos=(0, 0), units=None,
    labels=[1, 2, 3, 4, 5, 6], ticks=(1,2,3,4,5,6), granularity=0.1,
    style='rating', styleTweaks=('triangleMarker',), opacity=None,
    color='LightGray', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.02,
    flip=False, depth=-1, readOnly=False)
mouse_lowconf_3 = event.Mouse(win=win)
x, y = [None, None]
mouse_lowconf_3.mouseClock = core.Clock()
instructions3_3 = visual.TextStim(win=win, name='instructions3_3',
    text='Using the mouse, click on the line above to give your answer. A red triangle should appear to indicate your choice. Then press the ‘c’ key to continue.',
    font='Open Sans',
    pos=(0, -.3), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
key_resp_24 = keyboard.Keyboard()

# Initialize components for Routine "UncertaintyMoneyScale"
UncertaintyMoneyScaleClock = core.Clock()
uncertainty_money_q = visual.TextStim(win=win, name='uncertainty_money_q',
    text='When you were feeling uncertainty about a trial, to what extent do you think you based your final decision on the money?',
    font='Open Sans',
    pos=(0, .3), height=0.04, wrapWidth=1.2, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
uncertainty_money_q_response = visual.Slider(win=win, name='uncertainty_money_q_response',
    startValue=0, size=(1.0, 0.03), pos=(0, 0), units=None,
    labels=[1, 2, 3, 4, 5, 6], ticks=(1,2,3,4,5,6), granularity=0.1,
    style='rating', styleTweaks=('triangleMarker',), opacity=None,
    color='LightGray', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.02,
    flip=False, depth=-1, readOnly=False)
mouse_lowconf_4 = event.Mouse(win=win)
x, y = [None, None]
mouse_lowconf_4.mouseClock = core.Clock()
instructions3_4 = visual.TextStim(win=win, name='instructions3_4',
    text='Using the mouse, click on the line above to give your answer. A red triangle should appear to indicate your choice. Then press the ‘c’ key to continue.',
    font='Open Sans',
    pos=(0, -.3), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
key_resp_25 = keyboard.Keyboard()

# Initialize components for Routine "UncertaintyMemoryScale"
UncertaintyMemoryScaleClock = core.Clock()
uncertainty_memory_q = visual.TextStim(win=win, name='uncertainty_memory_q',
    text='When you were feeling uncertainty about a trial, to what extent do you think you based your final decision on your memory?',
    font='Open Sans',
    pos=(0, .3), height=0.04, wrapWidth=1.2, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
uncertainty_memory_q_response = visual.Slider(win=win, name='uncertainty_memory_q_response',
    startValue=0, size=(1.0, 0.03), pos=(0, 0), units=None,
    labels=[1, 2, 3, 4, 5, 6], ticks=(1,2,3,4,5,6), granularity=0.1,
    style='rating', styleTweaks=('triangleMarker',), opacity=None,
    color='LightGray', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.02,
    flip=False, depth=-1, readOnly=False)
mouse_lowconf_5 = event.Mouse(win=win)
x, y = [None, None]
mouse_lowconf_5.mouseClock = core.Clock()
instructions3_5 = visual.TextStim(win=win, name='instructions3_5',
    text='Using the mouse, click on the line above to give your answer. A red triangle should appear to indicate your choice. Then press the ‘c’ key to continue.',
    font='Open Sans',
    pos=(0, -.3), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
key_resp_26 = keyboard.Keyboard()

# Initialize components for Routine "Memory_or_Money_Binary"
Memory_or_Money_BinaryClock = core.Clock()
mem_or_money_q = visual.TextStim(win=win, name='mem_or_money_q',
    text='Would you say overall that your choices were based on your memory or the money?',
    font='Open Sans',
    pos=(0, .3), height=0.04, wrapWidth=1.2, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
mem_or_money_binary_response = visual.Slider(win=win, name='mem_or_money_binary_response',
    startValue=0, size=(1.0, 0.03), pos=(0, 0), units=None,
    labels=["memory","money"], ticks=(0,1), granularity=1.0,
    style='rating', styleTweaks=('triangleMarker',), opacity=None,
    color='LightGray', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.02,
    flip=False, depth=-1, readOnly=False)
mouse_lowconf_6 = event.Mouse(win=win)
x, y = [None, None]
mouse_lowconf_6.mouseClock = core.Clock()
instructions3_6 = visual.TextStim(win=win, name='instructions3_6',
    text='Using the mouse, click on the line above to give your answer. A red triangle should appear to indicate your choice. Then press the ‘c’ key to continue.',
    font='Open Sans',
    pos=(0, -.3), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
key_resp_27 = keyboard.Keyboard()

# Initialize components for Routine "Blank100"
Blank100Clock = core.Clock()
Blank_2 = visual.TextStim(win=win, name='Blank_2',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "FreeResponse_2"
FreeResponse_2Clock = core.Clock()
Question_2 = visual.TextStim(win=win, name='Question_2',
    text='Task Feedback\n\nDo you have any feedback or comments about the task?',
    font='Open Sans',
    pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
comments = visual.TextBox2(
     win, text='Please type your response here . . . ', font='Open Sans',
     pos=(0, 0),     letterHeight=0.02,
     size=(1.0, 0.03), borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=1.0,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0,
     anchor='center',
     fillColor='white', borderColor=None,
     flipHoriz=False, flipVert=False,
     editable=True,
     name='comments',
     autoLog=True,
)
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
Clickable_2 = visual.TextStim(win=win, name='Clickable_2',
    text='When finished, click here to continue. ',
    font='Open Sans',
    pos=(0.3, -0.3), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "FinishScreen"
FinishScreenClock = core.Clock()
thankyoumsg_2 = visual.TextStim(win=win, name='thankyoumsg_2',
    text='Great job!',
    font='Open Sans',
    pos=(0, .3), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
experimentearning = visual.TextStim(win=win, name='experimentearning',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=1.4, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_20 = keyboard.Keyboard()
text_6 = visual.TextStim(win=win, name='text_6',
    text='Please press the spacebar to continue.',
    font='Open Sans',
    pos=(0, -.35), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "EndMessage"
EndMessageClock = core.Clock()
thankyoumsg = visual.TextStim(win=win, name='thankyoumsg',
    text='You have completed the part two of the experiment.\n\nThank you! \n\nPress the ‘e’ key to exit.  \n',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_final = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Overall_Instruction"-------
continueRoutine = True
# update component parameters for each repeat
Overall_Instruction_key.keys = []
Overall_Instruction_key.rt = []
_Overall_Instruction_key_allKeys = []
# keep track of which components have finished
Overall_InstructionComponents = [Overall_Instruction_text, Overall_Instruction_key]
for thisComponent in Overall_InstructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Overall_InstructionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Overall_Instruction"-------
while continueRoutine:
    # get current time
    t = Overall_InstructionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Overall_InstructionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Overall_Instruction_text* updates
    if Overall_Instruction_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Overall_Instruction_text.frameNStart = frameN  # exact frame index
        Overall_Instruction_text.tStart = t  # local t and not account for scr refresh
        Overall_Instruction_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Overall_Instruction_text, 'tStartRefresh')  # time at next scr refresh
        Overall_Instruction_text.setAutoDraw(True)
    
    # *Overall_Instruction_key* updates
    waitOnFlip = False
    if Overall_Instruction_key.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
        # keep track of start time/frame for later
        Overall_Instruction_key.frameNStart = frameN  # exact frame index
        Overall_Instruction_key.tStart = t  # local t and not account for scr refresh
        Overall_Instruction_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Overall_Instruction_key, 'tStartRefresh')  # time at next scr refresh
        Overall_Instruction_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Overall_Instruction_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Overall_Instruction_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Overall_Instruction_key.status == STARTED and not waitOnFlip:
        theseKeys = Overall_Instruction_key.getKeys(keyList=['space'], waitRelease=False)
        _Overall_Instruction_key_allKeys.extend(theseKeys)
        if len(_Overall_Instruction_key_allKeys):
            Overall_Instruction_key.keys = _Overall_Instruction_key_allKeys[-1].name  # just the last key pressed
            Overall_Instruction_key.rt = _Overall_Instruction_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Overall_InstructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Overall_Instruction"-------
for thisComponent in Overall_InstructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Overall_Instruction_text.started', Overall_Instruction_text.tStartRefresh)
thisExp.addData('Overall_Instruction_text.stopped', Overall_Instruction_text.tStopRefresh)
# check responses
if Overall_Instruction_key.keys in ['', [], None]:  # No response was made
    Overall_Instruction_key.keys = None
thisExp.addData('Overall_Instruction_key.keys',Overall_Instruction_key.keys)
if Overall_Instruction_key.keys != None:  # we had a response
    thisExp.addData('Overall_Instruction_key.rt', Overall_Instruction_key.rt)
thisExp.addData('Overall_Instruction_key.started', Overall_Instruction_key.tStartRefresh)
thisExp.addData('Overall_Instruction_key.stopped', Overall_Instruction_key.tStopRefresh)
thisExp.nextEntry()
# the Routine "Overall_Instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Sound_Check"-------
continueRoutine = True
# update component parameters for each repeat
Overall_Instruction_key_2.keys = []
Overall_Instruction_key_2.rt = []
_Overall_Instruction_key_2_allKeys = []
sound_1.setSound('B', hamming=True)
sound_1.setVolume(0.5, log=False)
# keep track of which components have finished
Sound_CheckComponents = [Overall_Instruction_text_2, Overall_Instruction_key_2, sound_1, Continue]
for thisComponent in Sound_CheckComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Sound_CheckClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Sound_Check"-------
while continueRoutine:
    # get current time
    t = Sound_CheckClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Sound_CheckClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Overall_Instruction_text_2* updates
    if Overall_Instruction_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Overall_Instruction_text_2.frameNStart = frameN  # exact frame index
        Overall_Instruction_text_2.tStart = t  # local t and not account for scr refresh
        Overall_Instruction_text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Overall_Instruction_text_2, 'tStartRefresh')  # time at next scr refresh
        Overall_Instruction_text_2.setAutoDraw(True)
    
    # *Overall_Instruction_key_2* updates
    waitOnFlip = False
    if Overall_Instruction_key_2.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
        # keep track of start time/frame for later
        Overall_Instruction_key_2.frameNStart = frameN  # exact frame index
        Overall_Instruction_key_2.tStart = t  # local t and not account for scr refresh
        Overall_Instruction_key_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Overall_Instruction_key_2, 'tStartRefresh')  # time at next scr refresh
        Overall_Instruction_key_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Overall_Instruction_key_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Overall_Instruction_key_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Overall_Instruction_key_2.status == STARTED and not waitOnFlip:
        theseKeys = Overall_Instruction_key_2.getKeys(keyList=['space'], waitRelease=False)
        _Overall_Instruction_key_2_allKeys.extend(theseKeys)
        if len(_Overall_Instruction_key_2_allKeys):
            Overall_Instruction_key_2.keys = _Overall_Instruction_key_2_allKeys[-1].name  # just the last key pressed
            Overall_Instruction_key_2.rt = _Overall_Instruction_key_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    # start/stop sound_1
    if sound_1.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        sound_1.frameNStart = frameN  # exact frame index
        sound_1.tStart = t  # local t and not account for scr refresh
        sound_1.tStartRefresh = tThisFlipGlobal  # on global time
        sound_1.play(when=win)  # sync with win flip
    
    # *Continue* updates
    if Continue.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
        # keep track of start time/frame for later
        Continue.frameNStart = frameN  # exact frame index
        Continue.tStart = t  # local t and not account for scr refresh
        Continue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Continue, 'tStartRefresh')  # time at next scr refresh
        Continue.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Sound_CheckComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Sound_Check"-------
for thisComponent in Sound_CheckComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Overall_Instruction_text_2.started', Overall_Instruction_text_2.tStartRefresh)
thisExp.addData('Overall_Instruction_text_2.stopped', Overall_Instruction_text_2.tStopRefresh)
# check responses
if Overall_Instruction_key_2.keys in ['', [], None]:  # No response was made
    Overall_Instruction_key_2.keys = None
thisExp.addData('Overall_Instruction_key_2.keys',Overall_Instruction_key_2.keys)
if Overall_Instruction_key_2.keys != None:  # we had a response
    thisExp.addData('Overall_Instruction_key_2.rt', Overall_Instruction_key_2.rt)
thisExp.addData('Overall_Instruction_key_2.started', Overall_Instruction_key_2.tStartRefresh)
thisExp.addData('Overall_Instruction_key_2.stopped', Overall_Instruction_key_2.tStopRefresh)
thisExp.nextEntry()
sound_1.stop()  # ensure sound has stopped at end of routine
thisExp.addData('sound_1.started', sound_1.tStartRefresh)
thisExp.addData('sound_1.stopped', sound_1.tStopRefresh)
thisExp.addData('Continue.started', Continue.tStartRefresh)
thisExp.addData('Continue.stopped', Continue.tStopRefresh)
# the Routine "Sound_Check" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Now_The_Video_Will_Play"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_22.keys = []
key_resp_22.rt = []
_key_resp_22_allKeys = []
# keep track of which components have finished
Now_The_Video_Will_PlayComponents = [Overall_Instruction_text_3, key_resp_22, Continue_2]
for thisComponent in Now_The_Video_Will_PlayComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Now_The_Video_Will_PlayClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Now_The_Video_Will_Play"-------
while continueRoutine:
    # get current time
    t = Now_The_Video_Will_PlayClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Now_The_Video_Will_PlayClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Overall_Instruction_text_3* updates
    if Overall_Instruction_text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Overall_Instruction_text_3.frameNStart = frameN  # exact frame index
        Overall_Instruction_text_3.tStart = t  # local t and not account for scr refresh
        Overall_Instruction_text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Overall_Instruction_text_3, 'tStartRefresh')  # time at next scr refresh
        Overall_Instruction_text_3.setAutoDraw(True)
    
    # *key_resp_22* updates
    waitOnFlip = False
    if key_resp_22.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
        # keep track of start time/frame for later
        key_resp_22.frameNStart = frameN  # exact frame index
        key_resp_22.tStart = t  # local t and not account for scr refresh
        key_resp_22.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_22, 'tStartRefresh')  # time at next scr refresh
        key_resp_22.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_22.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_22.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_22.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_22.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_22_allKeys.extend(theseKeys)
        if len(_key_resp_22_allKeys):
            key_resp_22.keys = _key_resp_22_allKeys[-1].name  # just the last key pressed
            key_resp_22.rt = _key_resp_22_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *Continue_2* updates
    if Continue_2.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
        # keep track of start time/frame for later
        Continue_2.frameNStart = frameN  # exact frame index
        Continue_2.tStart = t  # local t and not account for scr refresh
        Continue_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Continue_2, 'tStartRefresh')  # time at next scr refresh
        Continue_2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Now_The_Video_Will_PlayComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Now_The_Video_Will_Play"-------
for thisComponent in Now_The_Video_Will_PlayComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Overall_Instruction_text_3.started', Overall_Instruction_text_3.tStartRefresh)
thisExp.addData('Overall_Instruction_text_3.stopped', Overall_Instruction_text_3.tStopRefresh)
# check responses
if key_resp_22.keys in ['', [], None]:  # No response was made
    key_resp_22.keys = None
thisExp.addData('key_resp_22.keys',key_resp_22.keys)
if key_resp_22.keys != None:  # we had a response
    thisExp.addData('key_resp_22.rt', key_resp_22.rt)
thisExp.addData('key_resp_22.started', key_resp_22.tStartRefresh)
thisExp.addData('key_resp_22.stopped', key_resp_22.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('Continue_2.started', Continue_2.tStartRefresh)
thisExp.addData('Continue_2.stopped', Continue_2.tStopRefresh)
# the Routine "Now_The_Video_Will_Play" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "videoInstructions"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
videoInstructionsComponents = [movie]
for thisComponent in videoInstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
videoInstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "videoInstructions"-------
while continueRoutine:
    # get current time
    t = videoInstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=videoInstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *movie* updates
    if movie.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        movie.frameNStart = frameN  # exact frame index
        movie.tStart = t  # local t and not account for scr refresh
        movie.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(movie, 'tStartRefresh')  # time at next scr refresh
        movie.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in videoInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "videoInstructions"-------
for thisComponent in videoInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
movie.stop()
# the Routine "videoInstructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Commitment_Do_Better_Response"-------
continueRoutine = True
# update component parameters for each repeat
commitment_question_response.reset()
# setup some python lists for storing info about the mouse_1
mouse_1.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
Commitment_Do_Better_ResponseComponents = [commitment_question, commitment_question_response, mouse_1, Clickable_1]
for thisComponent in Commitment_Do_Better_ResponseComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Commitment_Do_Better_ResponseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Commitment_Do_Better_Response"-------
while continueRoutine:
    # get current time
    t = Commitment_Do_Better_ResponseClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Commitment_Do_Better_ResponseClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *commitment_question* updates
    if commitment_question.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        commitment_question.frameNStart = frameN  # exact frame index
        commitment_question.tStart = t  # local t and not account for scr refresh
        commitment_question.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(commitment_question, 'tStartRefresh')  # time at next scr refresh
        commitment_question.setAutoDraw(True)
    
    # *commitment_question_response* updates
    if commitment_question_response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        commitment_question_response.frameNStart = frameN  # exact frame index
        commitment_question_response.tStart = t  # local t and not account for scr refresh
        commitment_question_response.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(commitment_question_response, 'tStartRefresh')  # time at next scr refresh
        commitment_question_response.setAutoDraw(True)
    # *mouse_1* updates
    if mouse_1.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_1.frameNStart = frameN  # exact frame index
        mouse_1.tStart = t  # local t and not account for scr refresh
        mouse_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_1, 'tStartRefresh')  # time at next scr refresh
        mouse_1.status = STARTED
        mouse_1.mouseClock.reset()
        prevButtonState = mouse_1.getPressed()  # if button is down already this ISN'T a new click
    if mouse_1.status == STARTED:  # only update if started and not finished!
        buttons = mouse_1.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(Clickable_1)
                    clickableList = Clickable_1
                except:
                    clickableList = [Clickable_1]
                for obj in clickableList:
                    if obj.contains(mouse_1):
                        gotValidClick = True
                        mouse_1.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # *Clickable_1* updates
    if Clickable_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Clickable_1.frameNStart = frameN  # exact frame index
        Clickable_1.tStart = t  # local t and not account for scr refresh
        Clickable_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Clickable_1, 'tStartRefresh')  # time at next scr refresh
        Clickable_1.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Commitment_Do_Better_ResponseComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Commitment_Do_Better_Response"-------
for thisComponent in Commitment_Do_Better_ResponseComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('commitment_question.started', commitment_question.tStartRefresh)
thisExp.addData('commitment_question.stopped', commitment_question.tStopRefresh)
thisExp.addData('commitment_question_response.text',commitment_question_response.text)
thisExp.addData('commitment_question_response.started', commitment_question_response.tStartRefresh)
thisExp.addData('commitment_question_response.stopped', commitment_question_response.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
thisExp.addData('Clickable_1.started', Clickable_1.tStartRefresh)
thisExp.addData('Clickable_1.stopped', Clickable_1.tStopRefresh)
# the Routine "Commitment_Do_Better_Response" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Code"-------
continueRoutine = True
# update component parameters for each repeat







"""

studyarray = [[None for _ in range(6)] for _ in range(12)]
testarray = [[None for _ in range(12)] for _ in range(12)]
i = 0
ss = []
ts = []

for j in range(12):
    i = j*2
    for k in range(6):
        studyarray[j][k] = stim_file[pics_per_block*i + k]
    for k in range(12):
        testarray[j][k] = stim_file[pics_per_block*i + k]
    console.log(ss)

console.log(studyarray)
console.log(testarray)

"""




# keep track of which components have finished
CodeComponents = []
for thisComponent in CodeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
CodeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Code"-------
while continueRoutine:
    # get current time
    t = CodeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=CodeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in CodeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Code"-------
for thisComponent in CodeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Code" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
blockloop = data.TrialHandler(nReps=num_blocks, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='blockloop')
thisExp.addLoop(blockloop)  # add the loop to the experiment
thisBlockloop = blockloop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlockloop.rgb)
if thisBlockloop != None:
    for paramName in thisBlockloop:
        exec('{} = thisBlockloop[paramName]'.format(paramName))

for thisBlockloop in blockloop:
    currentLoop = blockloop
    # abbreviate parameter names if possible (e.g. rgb = thisBlockloop.rgb)
    if thisBlockloop != None:
        for paramName in thisBlockloop:
            exec('{} = thisBlockloop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "OverallBlockCode"-------
    continueRoutine = True
    # update component parameters for each repeat
    # Overall block code
    
    stimtype = "face"
    studyformat = "inperson"
    
    theme_using=imagearray[themecounter]
    
    oldset_using = theme_using[0:num_study]
    newset_using = theme_using[num_study:pics_per_block]
    
    studyset_using = oldset_using
    
    # current study trial
    study_trial = 0
    
    studyblockmsg = "STUDY PHASE: " + str(blocknumber) + "/" + str(num_blocks)
    testblockmsg = "DECISION PHASE: " + str(blocknumber) + "/" + str(num_blocks)
    
    if blocknumber == 1 or blocknumber == 2 or blocknumber == 3 or blocknumber == 4:
        message_time = 10
        presentation_time = 0
    else:
        message_time = 0
        presentation_time = 0
    
    # keep track of which components have finished
    OverallBlockCodeComponents = []
    for thisComponent in OverallBlockCodeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    OverallBlockCodeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "OverallBlockCode"-------
    while continueRoutine:
        # get current time
        t = OverallBlockCodeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=OverallBlockCodeClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in OverallBlockCodeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "OverallBlockCode"-------
    for thisComponent in OverallBlockCodeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "OverallBlockCode" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "ReminderMessage"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_15.keys = []
    key_resp_15.rt = []
    _key_resp_15_allKeys = []
    # keep track of which components have finished
    ReminderMessageComponents = [studyreminder, key_resp_15]
    for thisComponent in ReminderMessageComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ReminderMessageClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ReminderMessage"-------
    while continueRoutine:
        # get current time
        t = ReminderMessageClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ReminderMessageClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *studyreminder* updates
        if studyreminder.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            studyreminder.frameNStart = frameN  # exact frame index
            studyreminder.tStart = t  # local t and not account for scr refresh
            studyreminder.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(studyreminder, 'tStartRefresh')  # time at next scr refresh
            studyreminder.setAutoDraw(True)
        if studyreminder.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > studyreminder.tStartRefresh + message_time-frameTolerance:
                # keep track of stop time/frame for later
                studyreminder.tStop = t  # not accounting for scr refresh
                studyreminder.frameNStop = frameN  # exact frame index
                win.timeOnFlip(studyreminder, 'tStopRefresh')  # time at next scr refresh
                studyreminder.setAutoDraw(False)
        
        # *key_resp_15* updates
        waitOnFlip = False
        if key_resp_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_15.frameNStart = frameN  # exact frame index
            key_resp_15.tStart = t  # local t and not account for scr refresh
            key_resp_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_15, 'tStartRefresh')  # time at next scr refresh
            key_resp_15.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_15.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_15.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_15.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_15.tStartRefresh + message_time-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_15.tStop = t  # not accounting for scr refresh
                key_resp_15.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_15, 'tStopRefresh')  # time at next scr refresh
                key_resp_15.status = FINISHED
        if key_resp_15.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_15.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
            _key_resp_15_allKeys.extend(theseKeys)
            if len(_key_resp_15_allKeys):
                key_resp_15.keys = _key_resp_15_allKeys[-1].name  # just the last key pressed
                key_resp_15.rt = _key_resp_15_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ReminderMessageComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ReminderMessage"-------
    for thisComponent in ReminderMessageComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    blockloop.addData('studyreminder.started', studyreminder.tStartRefresh)
    blockloop.addData('studyreminder.stopped', studyreminder.tStopRefresh)
    # check responses
    if key_resp_15.keys in ['', [], None]:  # No response was made
        key_resp_15.keys = None
    blockloop.addData('key_resp_15.keys',key_resp_15.keys)
    if key_resp_15.keys != None:  # we had a response
        blockloop.addData('key_resp_15.rt', key_resp_15.rt)
    blockloop.addData('key_resp_15.started', key_resp_15.tStartRefresh)
    blockloop.addData('key_resp_15.stopped', key_resp_15.tStopRefresh)
    # the Routine "ReminderMessage" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "StudyBlockMessage"-------
    continueRoutine = True
    # update component parameters for each repeat
    studyblockinfo.setText(studyblockmsg

)
    key_resp_proceed.keys = []
    key_resp_proceed.rt = []
    _key_resp_proceed_allKeys = []
    # keep track of which components have finished
    StudyBlockMessageComponents = [studyblockinfo, s_key, key_resp_proceed]
    for thisComponent in StudyBlockMessageComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    StudyBlockMessageClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "StudyBlockMessage"-------
    while continueRoutine:
        # get current time
        t = StudyBlockMessageClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=StudyBlockMessageClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *studyblockinfo* updates
        if studyblockinfo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            studyblockinfo.frameNStart = frameN  # exact frame index
            studyblockinfo.tStart = t  # local t and not account for scr refresh
            studyblockinfo.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(studyblockinfo, 'tStartRefresh')  # time at next scr refresh
            studyblockinfo.setAutoDraw(True)
        
        # *s_key* updates
        if s_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            s_key.frameNStart = frameN  # exact frame index
            s_key.tStart = t  # local t and not account for scr refresh
            s_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(s_key, 'tStartRefresh')  # time at next scr refresh
            s_key.setAutoDraw(True)
        
        # *key_resp_proceed* updates
        waitOnFlip = False
        if key_resp_proceed.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_proceed.frameNStart = frameN  # exact frame index
            key_resp_proceed.tStart = t  # local t and not account for scr refresh
            key_resp_proceed.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_proceed, 'tStartRefresh')  # time at next scr refresh
            key_resp_proceed.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_proceed.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_proceed.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_proceed.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_proceed.getKeys(keyList=['s', 'S'], waitRelease=False)
            _key_resp_proceed_allKeys.extend(theseKeys)
            if len(_key_resp_proceed_allKeys):
                key_resp_proceed.keys = _key_resp_proceed_allKeys[-1].name  # just the last key pressed
                key_resp_proceed.rt = _key_resp_proceed_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in StudyBlockMessageComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "StudyBlockMessage"-------
    for thisComponent in StudyBlockMessageComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    blockloop.addData('studyblockinfo.started', studyblockinfo.tStartRefresh)
    blockloop.addData('studyblockinfo.stopped', studyblockinfo.tStopRefresh)
    blockloop.addData('s_key.started', s_key.tStartRefresh)
    blockloop.addData('s_key.stopped', s_key.tStopRefresh)
    # check responses
    if key_resp_proceed.keys in ['', [], None]:  # No response was made
        key_resp_proceed.keys = None
    blockloop.addData('key_resp_proceed.keys',key_resp_proceed.keys)
    if key_resp_proceed.keys != None:  # we had a response
        blockloop.addData('key_resp_proceed.rt', key_resp_proceed.rt)
    # the Routine "StudyBlockMessage" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    studypicloop = data.TrialHandler(nReps=num_study, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='studypicloop')
    thisExp.addLoop(studypicloop)  # add the loop to the experiment
    thisStudypicloop = studypicloop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisStudypicloop.rgb)
    if thisStudypicloop != None:
        for paramName in thisStudypicloop:
            exec('{} = thisStudypicloop[paramName]'.format(paramName))
    
    for thisStudypicloop in studypicloop:
        currentLoop = studypicloop
        # abbreviate parameter names if possible (e.g. rgb = thisStudypicloop.rgb)
        if thisStudypicloop != None:
            for paramName in thisStudypicloop:
                exec('{} = thisStudypicloop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Code_StudyBlock"-------
        continueRoutine = True
        # update component parameters for each repeat
        # Code_StudyBlock
        
        FacePic = studyset_using[study_trial]
        
        thisExp.addData('imageShown',FacePic)
        # keep track of which components have finished
        Code_StudyBlockComponents = []
        for thisComponent in Code_StudyBlockComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Code_StudyBlockClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Code_StudyBlock"-------
        while continueRoutine:
            # get current time
            t = Code_StudyBlockClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Code_StudyBlockClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Code_StudyBlockComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Code_StudyBlock"-------
        for thisComponent in Code_StudyBlockComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "Code_StudyBlock" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "Learning_Trial"-------
        continueRoutine = True
        routineTimer.add(0.600000)
        # update component parameters for each repeat
        LearningImage.setSize((0.201, 0.256))
        LearningImage.setImage(FacePic)
        # keep track of which components have finished
        Learning_TrialComponents = [LearningImage]
        for thisComponent in Learning_TrialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Learning_TrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Learning_Trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = Learning_TrialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Learning_TrialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *LearningImage* updates
            if LearningImage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                LearningImage.frameNStart = frameN  # exact frame index
                LearningImage.tStart = t  # local t and not account for scr refresh
                LearningImage.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(LearningImage, 'tStartRefresh')  # time at next scr refresh
                LearningImage.setAutoDraw(True)
            if LearningImage.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > LearningImage.tStartRefresh + 0.6-frameTolerance:
                    # keep track of stop time/frame for later
                    LearningImage.tStop = t  # not accounting for scr refresh
                    LearningImage.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(LearningImage, 'tStopRefresh')  # time at next scr refresh
                    LearningImage.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Learning_TrialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Learning_Trial"-------
        for thisComponent in Learning_TrialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        studypicloop.addData('LearningImage.started', LearningImage.tStartRefresh)
        studypicloop.addData('LearningImage.stopped', LearningImage.tStopRefresh)
        
        # ------Prepare to start Routine "Blank300"-------
        continueRoutine = True
        routineTimer.add(0.200000)
        # update component parameters for each repeat
        # keep track of which components have finished
        Blank300Components = [polygon]
        for thisComponent in Blank300Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Blank300Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Blank300"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = Blank300Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Blank300Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *polygon* updates
            if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                polygon.frameNStart = frameN  # exact frame index
                polygon.tStart = t  # local t and not account for scr refresh
                polygon.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
                polygon.setAutoDraw(True)
            if polygon.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > polygon.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    polygon.tStop = t  # not accounting for scr refresh
                    polygon.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(polygon, 'tStopRefresh')  # time at next scr refresh
                    polygon.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Blank300Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Blank300"-------
        for thisComponent in Blank300Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        studypicloop.addData('polygon.started', polygon.tStartRefresh)
        studypicloop.addData('polygon.stopped', polygon.tStopRefresh)
        
        # ------Prepare to start Routine "studyloop"-------
        continueRoutine = True
        # update component parameters for each repeat
        study_trial = study_trial + 1
        # keep track of which components have finished
        studyloopComponents = []
        for thisComponent in studyloopComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        studyloopClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "studyloop"-------
        while continueRoutine:
            # get current time
            t = studyloopClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=studyloopClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in studyloopComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "studyloop"-------
        for thisComponent in studyloopComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "studyloop" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed num_study repeats of 'studypicloop'
    
    
    # ------Prepare to start Routine "TestBlockCode"-------
    continueRoutine = True
    # update component parameters for each repeat
    import random
    
    # Initialize variables
    concounter = 0  # Counter for some purpose
    condorder_now = cond_perm[condorder_counter]  # Current condition order
    
    blockpay = 0  # Variable for block payment
    testtrialnum = 1  # Number of the current test trial
    
    # Define the number of old items per test condition
    a = old_per_cond
    oldset_neu = oldset_using[0:a]  # Subset of old items for neutral condition
    oldset_con = oldset_using[a:a + a]  # Subset of old items for condition
    oldset_lib = oldset_using[a + a:a + a + a]  # Subset of old items for some other condition
    
    # Define the number of new items per test condition
    b = new_per_cond
    newset_neu = newset_using[0:b]  # Subset of new items for neutral condition
    newset_con = newset_using[b:b + b]  # Subset of new items for condition
    newset_lib = newset_using[b + b:b + b + b]  # Subset of new items for some other condition
    
    # Combine old and new items for different conditions
    testarray_neu = oldset_neu + newset_neu  # Combined array for the neutral condition
    testarray_con = oldset_con + newset_con  # Combined array for the condition
    testarray_lib = oldset_lib + newset_lib  # Combined array for some other condition
    
    # Shuffle the combined arrays using the random module
    random.shuffle(testarray_neu)  # Shuffling the neutral condition array
    random.shuffle(testarray_con)  # Shuffling the condition array
    random.shuffle(testarray_lib)  # Shuffling the other condition array
    # keep track of which components have finished
    TestBlockCodeComponents = []
    for thisComponent in TestBlockCodeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    TestBlockCodeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "TestBlockCode"-------
    while continueRoutine:
        # get current time
        t = TestBlockCodeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=TestBlockCodeClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TestBlockCodeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "TestBlockCode"-------
    for thisComponent in TestBlockCodeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "TestBlockCode" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "TestBlockMessage"-------
    continueRoutine = True
    # update component parameters for each repeat
    testblockreport.setText(testblockmsg)
    key_resp_proceed2.keys = []
    key_resp_proceed2.rt = []
    _key_resp_proceed2_allKeys = []
    # keep track of which components have finished
    TestBlockMessageComponents = [testblockreport, spacebar2, key_resp_proceed2]
    for thisComponent in TestBlockMessageComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    TestBlockMessageClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "TestBlockMessage"-------
    while continueRoutine:
        # get current time
        t = TestBlockMessageClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=TestBlockMessageClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *testblockreport* updates
        if testblockreport.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            testblockreport.frameNStart = frameN  # exact frame index
            testblockreport.tStart = t  # local t and not account for scr refresh
            testblockreport.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(testblockreport, 'tStartRefresh')  # time at next scr refresh
            testblockreport.setAutoDraw(True)
        
        # *spacebar2* updates
        if spacebar2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            spacebar2.frameNStart = frameN  # exact frame index
            spacebar2.tStart = t  # local t and not account for scr refresh
            spacebar2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(spacebar2, 'tStartRefresh')  # time at next scr refresh
            spacebar2.setAutoDraw(True)
        
        # *key_resp_proceed2* updates
        waitOnFlip = False
        if key_resp_proceed2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_proceed2.frameNStart = frameN  # exact frame index
            key_resp_proceed2.tStart = t  # local t and not account for scr refresh
            key_resp_proceed2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_proceed2, 'tStartRefresh')  # time at next scr refresh
            key_resp_proceed2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_proceed2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_proceed2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_proceed2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_proceed2.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_proceed2_allKeys.extend(theseKeys)
            if len(_key_resp_proceed2_allKeys):
                key_resp_proceed2.keys = _key_resp_proceed2_allKeys[-1].name  # just the last key pressed
                key_resp_proceed2.rt = _key_resp_proceed2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TestBlockMessageComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "TestBlockMessage"-------
    for thisComponent in TestBlockMessageComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    blockloop.addData('testblockreport.started', testblockreport.tStartRefresh)
    blockloop.addData('testblockreport.stopped', testblockreport.tStopRefresh)
    blockloop.addData('spacebar2.started', spacebar2.tStartRefresh)
    blockloop.addData('spacebar2.stopped', spacebar2.tStopRefresh)
    # check responses
    if key_resp_proceed2.keys in ['', [], None]:  # No response was made
        key_resp_proceed2.keys = None
    blockloop.addData('key_resp_proceed2.keys',key_resp_proceed2.keys)
    if key_resp_proceed2.keys != None:  # we had a response
        blockloop.addData('key_resp_proceed2.rt', key_resp_proceed2.rt)
    # the Routine "TestBlockMessage" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    conditionloop = data.TrialHandler(nReps=3.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='conditionloop')
    thisExp.addLoop(conditionloop)  # add the loop to the experiment
    thisConditionloop = conditionloop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisConditionloop.rgb)
    if thisConditionloop != None:
        for paramName in thisConditionloop:
            exec('{} = thisConditionloop[paramName]'.format(paramName))
    
    for thisConditionloop in conditionloop:
        currentLoop = conditionloop
        # abbreviate parameter names if possible (e.g. rgb = thisConditionloop.rgb)
        if thisConditionloop != None:
            for paramName in thisConditionloop:
                exec('{} = thisConditionloop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "CLNLoopCode"-------
        continueRoutine = True
        # update component parameters for each repeat
        # Extract the current condition from 'condorder_now' based on the value of 'concounter'
        conditionnow = condorder_now[concounter]
        
        # Reset the 'trialcounter' to 0 for the current trial
        trialcounter = 0
        
        # Add 'conditionnow' to the data collected in the experiment
        thisExp.addData('conditionnow', conditionnow)
        
        # keep track of which components have finished
        CLNLoopCodeComponents = []
        for thisComponent in CLNLoopCodeComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        CLNLoopCodeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "CLNLoopCode"-------
        while continueRoutine:
            # get current time
            t = CLNLoopCodeClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=CLNLoopCodeClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in CLNLoopCodeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "CLNLoopCode"-------
        for thisComponent in CLNLoopCodeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "CLNLoopCode" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "TestBlock_Select"-------
        continueRoutine = True
        # update component parameters for each repeat
        # Define the point system for the decision phase based on the current condition
        if conditionnow == 1:
            # Condition: conservative
            condition = "conservative"
            hit_reward = 5
            cr_reward = 5
            miss_loss = 0
            miss_loss_msg = "Lose 0 points"
            miss_loss_trial = "0 points incorrect"
            fa_loss = -20
            fa_loss_trial = "-20 points incorrect"
            pay_msg = "Incorrect OLD loses 20"
            fa_loss_msg = "Lose 20 points"
            testset_using = testarray_con
        elif conditionnow == 2:
            # Condition: liberal
            condition = "liberal"
            hit_reward = 5
            cr_reward = 5
            miss_loss = -20
            miss_loss_trial = "-20 points incorrect"
            miss_loss_msg = "Lose 20 points"
            fa_loss = 0
            fa_loss_trial = "0 points incorrect"
            pay_msg = "Incorrect NEW loses 20"
            fa_loss_msg = "Lose 0 points"
            testset_using = testarray_lib
        else: 
            # Condition: neutral
            condition = "neutral"
            hit_reward = 5
            cr_reward = 5
            miss_loss = 0
            miss_loss_msg = "Lose 0 points"
            miss_loss_trial = "0 points incorrect"
            fa_loss = 0
            fa_loss_trial = "0 points incorrect"
            pay_msg = "No loss for incorrect choices"
            fa_loss_msg = "Lose 0 points"
            testset_using = testarray_neu
        
        # keep track of which components have finished
        TestBlock_SelectComponents = []
        for thisComponent in TestBlock_SelectComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        TestBlock_SelectClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "TestBlock_Select"-------
        while continueRoutine:
            # get current time
            t = TestBlock_SelectClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=TestBlock_SelectClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in TestBlock_SelectComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "TestBlock_Select"-------
        for thisComponent in TestBlock_SelectComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "TestBlock_Select" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "Payoff_InfoScreen"-------
        continueRoutine = True
        # update component parameters for each repeat
        payalert.setText(pay_msg)
        key_resp_12.keys = []
        key_resp_12.rt = []
        _key_resp_12_allKeys = []
        # keep track of which components have finished
        Payoff_InfoScreenComponents = [text_correctpayoff, payalert, press_p, key_resp_12]
        for thisComponent in Payoff_InfoScreenComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Payoff_InfoScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Payoff_InfoScreen"-------
        while continueRoutine:
            # get current time
            t = Payoff_InfoScreenClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Payoff_InfoScreenClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_correctpayoff* updates
            if text_correctpayoff.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_correctpayoff.frameNStart = frameN  # exact frame index
                text_correctpayoff.tStart = t  # local t and not account for scr refresh
                text_correctpayoff.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_correctpayoff, 'tStartRefresh')  # time at next scr refresh
                text_correctpayoff.setAutoDraw(True)
            
            # *payalert* updates
            if payalert.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                payalert.frameNStart = frameN  # exact frame index
                payalert.tStart = t  # local t and not account for scr refresh
                payalert.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(payalert, 'tStartRefresh')  # time at next scr refresh
                payalert.setAutoDraw(True)
            
            # *press_p* updates
            if press_p.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                press_p.frameNStart = frameN  # exact frame index
                press_p.tStart = t  # local t and not account for scr refresh
                press_p.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(press_p, 'tStartRefresh')  # time at next scr refresh
                press_p.setAutoDraw(True)
            
            # *key_resp_12* updates
            waitOnFlip = False
            if key_resp_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_12.frameNStart = frameN  # exact frame index
                key_resp_12.tStart = t  # local t and not account for scr refresh
                key_resp_12.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_12, 'tStartRefresh')  # time at next scr refresh
                key_resp_12.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_12.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_12.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_12.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_12.getKeys(keyList=['p'], waitRelease=False)
                _key_resp_12_allKeys.extend(theseKeys)
                if len(_key_resp_12_allKeys):
                    key_resp_12.keys = _key_resp_12_allKeys[-1].name  # just the last key pressed
                    key_resp_12.rt = _key_resp_12_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Payoff_InfoScreenComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Payoff_InfoScreen"-------
        for thisComponent in Payoff_InfoScreenComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        conditionloop.addData('text_correctpayoff.started', text_correctpayoff.tStartRefresh)
        conditionloop.addData('text_correctpayoff.stopped', text_correctpayoff.tStopRefresh)
        conditionloop.addData('payalert.started', payalert.tStartRefresh)
        conditionloop.addData('payalert.stopped', payalert.tStopRefresh)
        conditionloop.addData('press_p.started', press_p.tStartRefresh)
        conditionloop.addData('press_p.stopped', press_p.tStopRefresh)
        # check responses
        if key_resp_12.keys in ['', [], None]:  # No response was made
            key_resp_12.keys = None
        conditionloop.addData('key_resp_12.keys',key_resp_12.keys)
        if key_resp_12.keys != None:  # we had a response
            conditionloop.addData('key_resp_12.rt', key_resp_12.rt)
        conditionloop.addData('key_resp_12.started', key_resp_12.tStartRefresh)
        conditionloop.addData('key_resp_12.stopped', key_resp_12.tStopRefresh)
        # the Routine "Payoff_InfoScreen" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        testpicloop = data.TrialHandler(nReps=num_test, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='testpicloop')
        thisExp.addLoop(testpicloop)  # add the loop to the experiment
        thisTestpicloop = testpicloop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTestpicloop.rgb)
        if thisTestpicloop != None:
            for paramName in thisTestpicloop:
                exec('{} = thisTestpicloop[paramName]'.format(paramName))
        
        for thisTestpicloop in testpicloop:
            currentLoop = testpicloop
            # abbreviate parameter names if possible (e.g. rgb = thisTestpicloop.rgb)
            if thisTestpicloop != None:
                for paramName in thisTestpicloop:
                    exec('{} = thisTestpicloop[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "Code_TestBlock"-------
            continueRoutine = True
            # update component parameters for each repeat
            # Assigning the study item for the test phase
            # If we do not randomize, use the item based on the current trial counter
            FacePic_test = testset_using[trialcounter]
            
            # Check if the current FacePic_test is in the studyset_using list
            if str(FacePic_test) in studyset_using:
                good_job = "j"  # If it's in the list, assign 'j' to good_job
            else:
                good_job = "k"  # If it's not in the list, assign 'k' to good_job
            
            # Determine the value of 'imagetruth' based on the presence of FacePic_test in studyset_using
            if str(FacePic_test) in studyset_using:
                 imagetruth = "old"  # If it's in the list, set 'imagetruth' to 'old'
            else:
                 imagetruth = "new"  # If it's not in the list, set 'imagetruth' to 'new'
            
            # Add relevant data to the experiment log
            thisExp.addData('condition', condition)
            thisExp.addData('imageShown', FacePic_test)
            thisExp.addData('imageTruth', imagetruth)
            thisExp.addData('correctkey', good_job)
            
            # keep track of which components have finished
            Code_TestBlockComponents = []
            for thisComponent in Code_TestBlockComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            Code_TestBlockClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "Code_TestBlock"-------
            while continueRoutine:
                # get current time
                t = Code_TestBlockClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=Code_TestBlockClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Code_TestBlockComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "Code_TestBlock"-------
            for thisComponent in Code_TestBlockComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # the Routine "Code_TestBlock" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "TestTrial"-------
            continueRoutine = True
            # update component parameters for each repeat
            Learning_TestTrial.setImage(FacePic_test)
            NEW.setText('k = NEW')
            Old_Points_minus.setText(fa_loss_trial)
            Points_add_Old.setText('+5  points correct')
            New_Points_minus.setText(miss_loss_trial)
            TestTrialKey.keys = []
            TestTrialKey.rt = []
            _TestTrialKey_allKeys = []
            # keep track of which components have finished
            TestTrialComponents = [Learning_TestTrial, OLD, NEW, Old_Points_minus, Points_add_Old, New_Points_minus, Points_Add_New, TestTrialKey]
            for thisComponent in TestTrialComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            TestTrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "TestTrial"-------
            while continueRoutine:
                # get current time
                t = TestTrialClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=TestTrialClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *Learning_TestTrial* updates
                if Learning_TestTrial.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Learning_TestTrial.frameNStart = frameN  # exact frame index
                    Learning_TestTrial.tStart = t  # local t and not account for scr refresh
                    Learning_TestTrial.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Learning_TestTrial, 'tStartRefresh')  # time at next scr refresh
                    Learning_TestTrial.setAutoDraw(True)
                
                # *OLD* updates
                if OLD.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    OLD.frameNStart = frameN  # exact frame index
                    OLD.tStart = t  # local t and not account for scr refresh
                    OLD.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(OLD, 'tStartRefresh')  # time at next scr refresh
                    OLD.setAutoDraw(True)
                if OLD.status == STARTED:  # only update if drawing
                    OLD.setColor('white', colorSpace='rgb', log=False)
                
                # *NEW* updates
                if NEW.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    NEW.frameNStart = frameN  # exact frame index
                    NEW.tStart = t  # local t and not account for scr refresh
                    NEW.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(NEW, 'tStartRefresh')  # time at next scr refresh
                    NEW.setAutoDraw(True)
                
                # *Old_Points_minus* updates
                if Old_Points_minus.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Old_Points_minus.frameNStart = frameN  # exact frame index
                    Old_Points_minus.tStart = t  # local t and not account for scr refresh
                    Old_Points_minus.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Old_Points_minus, 'tStartRefresh')  # time at next scr refresh
                    Old_Points_minus.setAutoDraw(True)
                
                # *Points_add_Old* updates
                if Points_add_Old.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Points_add_Old.frameNStart = frameN  # exact frame index
                    Points_add_Old.tStart = t  # local t and not account for scr refresh
                    Points_add_Old.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Points_add_Old, 'tStartRefresh')  # time at next scr refresh
                    Points_add_Old.setAutoDraw(True)
                
                # *New_Points_minus* updates
                if New_Points_minus.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    New_Points_minus.frameNStart = frameN  # exact frame index
                    New_Points_minus.tStart = t  # local t and not account for scr refresh
                    New_Points_minus.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(New_Points_minus, 'tStartRefresh')  # time at next scr refresh
                    New_Points_minus.setAutoDraw(True)
                
                # *Points_Add_New* updates
                if Points_Add_New.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Points_Add_New.frameNStart = frameN  # exact frame index
                    Points_Add_New.tStart = t  # local t and not account for scr refresh
                    Points_Add_New.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Points_Add_New, 'tStartRefresh')  # time at next scr refresh
                    Points_Add_New.setAutoDraw(True)
                
                # *TestTrialKey* updates
                waitOnFlip = False
                if TestTrialKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    TestTrialKey.frameNStart = frameN  # exact frame index
                    TestTrialKey.tStart = t  # local t and not account for scr refresh
                    TestTrialKey.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(TestTrialKey, 'tStartRefresh')  # time at next scr refresh
                    TestTrialKey.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(TestTrialKey.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(TestTrialKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if TestTrialKey.status == STARTED and not waitOnFlip:
                    theseKeys = TestTrialKey.getKeys(keyList=['j', 'k'], waitRelease=False)
                    _TestTrialKey_allKeys.extend(theseKeys)
                    if len(_TestTrialKey_allKeys):
                        TestTrialKey.keys = _TestTrialKey_allKeys[-1].name  # just the last key pressed
                        TestTrialKey.rt = _TestTrialKey_allKeys[-1].rt
                        # was this correct?
                        if (TestTrialKey.keys == str(good_job)) or (TestTrialKey.keys == good_job):
                            TestTrialKey.corr = 1
                        else:
                            TestTrialKey.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in TestTrialComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "TestTrial"-------
            for thisComponent in TestTrialComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            testpicloop.addData('Learning_TestTrial.started', Learning_TestTrial.tStartRefresh)
            testpicloop.addData('Learning_TestTrial.stopped', Learning_TestTrial.tStopRefresh)
            testpicloop.addData('OLD.started', OLD.tStartRefresh)
            testpicloop.addData('OLD.stopped', OLD.tStopRefresh)
            testpicloop.addData('NEW.started', NEW.tStartRefresh)
            testpicloop.addData('NEW.stopped', NEW.tStopRefresh)
            testpicloop.addData('Old_Points_minus.started', Old_Points_minus.tStartRefresh)
            testpicloop.addData('Old_Points_minus.stopped', Old_Points_minus.tStopRefresh)
            testpicloop.addData('Points_add_Old.started', Points_add_Old.tStartRefresh)
            testpicloop.addData('Points_add_Old.stopped', Points_add_Old.tStopRefresh)
            testpicloop.addData('New_Points_minus.started', New_Points_minus.tStartRefresh)
            testpicloop.addData('New_Points_minus.stopped', New_Points_minus.tStopRefresh)
            testpicloop.addData('Points_Add_New.started', Points_Add_New.tStartRefresh)
            testpicloop.addData('Points_Add_New.stopped', Points_Add_New.tStopRefresh)
            # check responses
            if TestTrialKey.keys in ['', [], None]:  # No response was made
                TestTrialKey.keys = None
                # was no response the correct answer?!
                if str(good_job).lower() == 'none':
                   TestTrialKey.corr = 1;  # correct non-response
                else:
                   TestTrialKey.corr = 0;  # failed to respond (incorrectly)
            # store data for testpicloop (TrialHandler)
            testpicloop.addData('TestTrialKey.keys',TestTrialKey.keys)
            testpicloop.addData('TestTrialKey.corr', TestTrialKey.corr)
            if TestTrialKey.keys != None:  # we had a response
                testpicloop.addData('TestTrialKey.rt', TestTrialKey.rt)
            testpicloop.addData('TestTrialKey.started', TestTrialKey.tStartRefresh)
            testpicloop.addData('TestTrialKey.stopped', TestTrialKey.tStopRefresh)
            # the Routine "TestTrial" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "updatepay"-------
            continueRoutine = True
            # update component parameters for each repeat
            # Reward_number stores earnings across the entire experiment
            
            conditions = {
                ('old', 'j'): (float(hit_reward), "hit"),
                ('new', 'k'): (float(cr_reward), "cr"),
                ('new', 'j'): (float(fa_loss), "fa"),
                ('old', 'k'): (float(miss_loss), "miss")
            }
            
            if (imagetruth, TestTrialKey.keys) in conditions:
                reward, responsetype = conditions[(imagetruth, TestTrialKey.keys)]
                reward_number = float(reward_number) + reward
                trialpay = reward
                blockpay = float(blockpay) + reward
            else:
                reward_number = float(reward_number)
                trialpay = 0
                blockpay = float(blockpay)
            
            thisExp.addData('blocknumber', blocknumber)
            thisExp.addData('totaltrialnum', totaltrialnum)
            thisExp.addData('testtrialnum', testtrialnum)
            thisExp.addData('responsetype', responsetype)
            thisExp.addData('trialpay', trialpay)
            thisExp.addData('blockpay', blockpay)
            thisExp.addData('totalpay', reward_number)
            thisExp.addData('hit_reward', hit_reward)
            thisExp.addData('cr_reward', cr_reward)
            thisExp.addData('fa_loss', fa_loss)
            thisExp.addData('miss_loss', miss_loss)
            
            blockreport_earning = f"Earnings for this block = {blockpay}"
            total_earning = f"Total earnings = {reward_number}"
            report_earning = f"Total earnings so far = {reward_number}"
            exptotal_earning = f"Total earnings for the experiment = {reward_number} points"
            
            # Determine the 'recogresponse' based on the value of 'TestTrialKey.keys'
            # If 'TestTrialKey.keys' is 'j', set 'recogresponse' to "old", otherwise set it to "new"
            recogresponse = "old" if TestTrialKey.keys == 'j' else "new"
            
            # Determine the 'idealconfidence' based on the value of 'TestTrialKey.corr'
            # If 'TestTrialKey.corr' is 1, set 'idealconfidence' to "high", otherwise set it to "low"
            idealconfidence = "high" if TestTrialKey.corr == 1 else "low"
            
            # Add 'recogresponse' and 'idealconfidence' to the data collected in the experiment
            thisExp.addData('recogresponse', recogresponse)
            thisExp.addData('idealconfidence', idealconfidence)
            
            # keep track of which components have finished
            updatepayComponents = []
            for thisComponent in updatepayComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            updatepayClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "updatepay"-------
            while continueRoutine:
                # get current time
                t = updatepayClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=updatepayClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in updatepayComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "updatepay"-------
            for thisComponent in updatepayComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # the Routine "updatepay" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "ConfidenceRating"-------
            continueRoutine = True
            # update component parameters for each repeat
            key_resp_confidence.keys = []
            key_resp_confidence.rt = []
            _key_resp_confidence_allKeys = []
            # keep track of which components have finished
            ConfidenceRatingComponents = [LT_Block_1_Confidence, key_resp_confidence]
            for thisComponent in ConfidenceRatingComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            ConfidenceRatingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "ConfidenceRating"-------
            while continueRoutine:
                # get current time
                t = ConfidenceRatingClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=ConfidenceRatingClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *LT_Block_1_Confidence* updates
                if LT_Block_1_Confidence.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    LT_Block_1_Confidence.frameNStart = frameN  # exact frame index
                    LT_Block_1_Confidence.tStart = t  # local t and not account for scr refresh
                    LT_Block_1_Confidence.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(LT_Block_1_Confidence, 'tStartRefresh')  # time at next scr refresh
                    LT_Block_1_Confidence.setAutoDraw(True)
                
                # *key_resp_confidence* updates
                waitOnFlip = False
                if key_resp_confidence.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_confidence.frameNStart = frameN  # exact frame index
                    key_resp_confidence.tStart = t  # local t and not account for scr refresh
                    key_resp_confidence.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_confidence, 'tStartRefresh')  # time at next scr refresh
                    key_resp_confidence.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_confidence.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_confidence.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_confidence.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_confidence.getKeys(keyList=['f', 'd', 's'], waitRelease=False)
                    _key_resp_confidence_allKeys.extend(theseKeys)
                    if len(_key_resp_confidence_allKeys):
                        key_resp_confidence.keys = _key_resp_confidence_allKeys[-1].name  # just the last key pressed
                        key_resp_confidence.rt = _key_resp_confidence_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ConfidenceRatingComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "ConfidenceRating"-------
            for thisComponent in ConfidenceRatingComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if key_resp_confidence.keys in ['', [], None]:  # No response was made
                key_resp_confidence.keys = None
            testpicloop.addData('key_resp_confidence.keys',key_resp_confidence.keys)
            if key_resp_confidence.keys != None:  # we had a response
                testpicloop.addData('key_resp_confidence.rt', key_resp_confidence.rt)
            testpicloop.addData('key_resp_confidence.started', key_resp_confidence.tStartRefresh)
            testpicloop.addData('key_resp_confidence.stopped', key_resp_confidence.tStopRefresh)
            # the Routine "ConfidenceRating" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "Running_Report"-------
            continueRoutine = True
            # update component parameters for each repeat
            # Define a dictionary to map keys to confidence responses
            key_to_confidence = {
                'f': "high",
                'd': "medium",
                's': "low"
            }
            
            # Set 'confidenceresp' based on the key response from 'key_resp_confidence'
            confidenceresp = key_to_confidence.get(key_resp_confidence.keys, None)
            
            thisExp.addData('confidenceresponse', confidenceresp)
            
            # keep track of which components have finished
            Running_ReportComponents = []
            for thisComponent in Running_ReportComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            Running_ReportClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "Running_Report"-------
            while continueRoutine:
                # get current time
                t = Running_ReportClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=Running_ReportClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Running_ReportComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "Running_Report"-------
            for thisComponent in Running_ReportComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # the Routine "Running_Report" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "JustBlank"-------
            continueRoutine = True
            routineTimer.add(0.200000)
            # update component parameters for each repeat
            # keep track of which components have finished
            JustBlankComponents = [text_9]
            for thisComponent in JustBlankComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            JustBlankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "JustBlank"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = JustBlankClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=JustBlankClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *text_9* updates
                if text_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_9.frameNStart = frameN  # exact frame index
                    text_9.tStart = t  # local t and not account for scr refresh
                    text_9.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
                    text_9.setAutoDraw(True)
                if text_9.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_9.tStartRefresh + 0.2-frameTolerance:
                        # keep track of stop time/frame for later
                        text_9.tStop = t  # not accounting for scr refresh
                        text_9.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(text_9, 'tStopRefresh')  # time at next scr refresh
                        text_9.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in JustBlankComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "JustBlank"-------
            for thisComponent in JustBlankComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            testpicloop.addData('text_9.started', text_9.tStartRefresh)
            testpicloop.addData('text_9.stopped', text_9.tStopRefresh)
            
            # ------Prepare to start Routine "testloop"-------
            continueRoutine = True
            # update component parameters for each repeat
            # Increment the variable 'trialcounter' by 1
            trialcounter += 1
            
            # Increment the variable 'testtrialnum' by 1
            testtrialnum += 1
            
            # Increment the variable 'totaltrialnum' by 1
            totaltrialnum += 1
            
            # keep track of which components have finished
            testloopComponents = []
            for thisComponent in testloopComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            testloopClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "testloop"-------
            while continueRoutine:
                # get current time
                t = testloopClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=testloopClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in testloopComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "testloop"-------
            for thisComponent in testloopComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # the Routine "testloop" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed num_test repeats of 'testpicloop'
        
        
        # ------Prepare to start Routine "Update_CLN"-------
        continueRoutine = True
        # update component parameters for each repeat
        # Increment concounter by 1
        concounter += 1
        # keep track of which components have finished
        Update_CLNComponents = []
        for thisComponent in Update_CLNComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Update_CLNClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Update_CLN"-------
        while continueRoutine:
            # get current time
            t = Update_CLNClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Update_CLNClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Update_CLNComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Update_CLN"-------
        for thisComponent in Update_CLNComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "Update_CLN" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 3.0 repeats of 'conditionloop'
    
    
    # ------Prepare to start Routine "BlockReport"-------
    continueRoutine = True
    # update component parameters for each repeat
    blockreportearn.setText(blockreport_earning)
    total_earning_report.setText(report_earning)
    key_resp_11.keys = []
    key_resp_11.rt = []
    _key_resp_11_allKeys = []
    # keep track of which components have finished
    BlockReportComponents = [blockreportearn, total_earning_report, spacetocontinue, key_resp_11]
    for thisComponent in BlockReportComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    BlockReportClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "BlockReport"-------
    while continueRoutine:
        # get current time
        t = BlockReportClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=BlockReportClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blockreportearn* updates
        if blockreportearn.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blockreportearn.frameNStart = frameN  # exact frame index
            blockreportearn.tStart = t  # local t and not account for scr refresh
            blockreportearn.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blockreportearn, 'tStartRefresh')  # time at next scr refresh
            blockreportearn.setAutoDraw(True)
        
        # *total_earning_report* updates
        if total_earning_report.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            total_earning_report.frameNStart = frameN  # exact frame index
            total_earning_report.tStart = t  # local t and not account for scr refresh
            total_earning_report.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(total_earning_report, 'tStartRefresh')  # time at next scr refresh
            total_earning_report.setAutoDraw(True)
        
        # *spacetocontinue* updates
        if spacetocontinue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            spacetocontinue.frameNStart = frameN  # exact frame index
            spacetocontinue.tStart = t  # local t and not account for scr refresh
            spacetocontinue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(spacetocontinue, 'tStartRefresh')  # time at next scr refresh
            spacetocontinue.setAutoDraw(True)
        
        # *key_resp_11* updates
        waitOnFlip = False
        if key_resp_11.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            key_resp_11.frameNStart = frameN  # exact frame index
            key_resp_11.tStart = t  # local t and not account for scr refresh
            key_resp_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_11, 'tStartRefresh')  # time at next scr refresh
            key_resp_11.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_11.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_11.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_11.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_11.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_11_allKeys.extend(theseKeys)
            if len(_key_resp_11_allKeys):
                key_resp_11.keys = _key_resp_11_allKeys[-1].name  # just the last key pressed
                key_resp_11.rt = _key_resp_11_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BlockReportComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "BlockReport"-------
    for thisComponent in BlockReportComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_11.keys in ['', [], None]:  # No response was made
        key_resp_11.keys = None
    blockloop.addData('key_resp_11.keys',key_resp_11.keys)
    if key_resp_11.keys != None:  # we had a response
        blockloop.addData('key_resp_11.rt', key_resp_11.rt)
    # the Routine "BlockReport" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "blockadvance"-------
    continueRoutine = True
    # update component parameters for each repeat
    # Increment the variable 'blockn' by 1
    blockn += 1
    
    # Increment the variable 'themecounter' by 1
    themecounter += 1
    
    # Increment the variable 'condorder_counter' by 1
    condorder_counter += 1
    
    # Increment the variable 'blocknumber' by 1
    blocknumber += 1
    
    # keep track of which components have finished
    blockadvanceComponents = []
    for thisComponent in blockadvanceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blockadvanceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blockadvance"-------
    while continueRoutine:
        # get current time
        t = blockadvanceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blockadvanceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blockadvanceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blockadvance"-------
    for thisComponent in blockadvanceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "blockadvance" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed num_blocks repeats of 'blockloop'


# ------Prepare to start Routine "EndVariables"-------
continueRoutine = True
# update component parameters for each repeat
# session number will serve as prevscore
prevscore = expInfo['session']
prevscore = float(prevscore)

reward_difference = reward_number - prevscore

# Determine the appropriate message and dollar amount based on the reward difference
if reward_difference > 0:
    if reward_difference >= 500:
        dollar_amount = "5"
    elif 400 <= reward_difference < 500:
        dollar_amount = "4"
    elif 300 <= reward_difference < 400:
        dollar_amount = "3"
    elif 200 <= reward_difference < 300:
        dollar_amount = "2"
    elif 100 <= reward_difference < 200:
        dollar_amount = "1"
    else:
        dollar_amount = "0"
    message = "you've earned a bonus of $" + dollar_amount + "."
    if reward_difference > 0:
        exptotal_earning = "You earned " + str(abs(reward_difference)) + " more points (" + str(reward_number) + "), which means " + message
    else:
        exptotal_earning = "You got the same amount of " + str(abs(reward_difference)) + " fewer points (" + str(reward_number) + "), which means " + message
else:
    if reward_difference == 0:
        exptotal_earning = "You got the same amount of points (" + str(reward_number) + "), which means you didn't earn a bonus this time."
    else:
        exptotal_earning = "You earned " + str(abs(reward_difference)) + " fewer points (" + str(reward_number) + "), which means you didn't earn a bonus this time."

# Add the experiment earning message to the data with a specific tag

thisExp.addData('final_experiment_earning', reward_number)
thisExp.addData('baseline_score', prevscore)
thisExp.addData('reward_difference', reward_difference)
thisExp.addData('final_experiment_bonus_message', exptotal_earning)

# keep track of which components have finished
EndVariablesComponents = []
for thisComponent in EndVariablesComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndVariablesClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "EndVariables"-------
while continueRoutine:
    # get current time
    t = EndVariablesClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndVariablesClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndVariablesComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "EndVariables"-------
for thisComponent in EndVariablesComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "EndVariables" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank100"-------
continueRoutine = True
routineTimer.add(0.100000)
# update component parameters for each repeat
# keep track of which components have finished
Blank100Components = [Blank_2]
for thisComponent in Blank100Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Blank100Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Blank100"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Blank100Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Blank100Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Blank_2* updates
    if Blank_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Blank_2.frameNStart = frameN  # exact frame index
        Blank_2.tStart = t  # local t and not account for scr refresh
        Blank_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Blank_2, 'tStartRefresh')  # time at next scr refresh
        Blank_2.setAutoDraw(True)
    if Blank_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Blank_2.tStartRefresh + 0.1-frameTolerance:
            # keep track of stop time/frame for later
            Blank_2.tStop = t  # not accounting for scr refresh
            Blank_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Blank_2, 'tStopRefresh')  # time at next scr refresh
            Blank_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Blank100Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Blank100"-------
for thisComponent in Blank100Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Blank_2.started', Blank_2.tStartRefresh)
thisExp.addData('Blank_2.stopped', Blank_2.tStopRefresh)

# ------Prepare to start Routine "QuestionProb"-------
continueRoutine = True
# update component parameters for each repeat
probold_slider.reset()
# setup some python lists for storing info about the mouse_probold
mouse_probold.clicked_name = []
gotValidClick = False  # until a click is received
key_resp_16.keys = []
key_resp_16.rt = []
_key_resp_16_allKeys = []
# keep track of which components have finished
QuestionProbComponents = [probq, probold_slider, mouse_probold, instructions, key_resp_16]
for thisComponent in QuestionProbComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
QuestionProbClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "QuestionProb"-------
while continueRoutine:
    # get current time
    t = QuestionProbClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=QuestionProbClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *probq* updates
    if probq.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        probq.frameNStart = frameN  # exact frame index
        probq.tStart = t  # local t and not account for scr refresh
        probq.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(probq, 'tStartRefresh')  # time at next scr refresh
        probq.setAutoDraw(True)
    
    # *probold_slider* updates
    if probold_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        probold_slider.frameNStart = frameN  # exact frame index
        probold_slider.tStart = t  # local t and not account for scr refresh
        probold_slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(probold_slider, 'tStartRefresh')  # time at next scr refresh
        probold_slider.setAutoDraw(True)
    
    # *instructions* updates
    if instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions.frameNStart = frameN  # exact frame index
        instructions.tStart = t  # local t and not account for scr refresh
        instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions, 'tStartRefresh')  # time at next scr refresh
        instructions.setAutoDraw(True)
    
    # *key_resp_16* updates
    waitOnFlip = False
    if key_resp_16.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
        # keep track of start time/frame for later
        key_resp_16.frameNStart = frameN  # exact frame index
        key_resp_16.tStart = t  # local t and not account for scr refresh
        key_resp_16.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_16, 'tStartRefresh')  # time at next scr refresh
        key_resp_16.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_16.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_16.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_16.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_16.getKeys(keyList=['c', 'C'], waitRelease=False)
        _key_resp_16_allKeys.extend(theseKeys)
        if len(_key_resp_16_allKeys):
            key_resp_16.keys = _key_resp_16_allKeys[-1].name  # just the last key pressed
            key_resp_16.rt = _key_resp_16_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in QuestionProbComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "QuestionProb"-------
for thisComponent in QuestionProbComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('probq.started', probq.tStartRefresh)
thisExp.addData('probq.stopped', probq.tStopRefresh)
thisExp.addData('probold_slider.response', probold_slider.getRating())
thisExp.addData('probold_slider.rt', probold_slider.getRT())
thisExp.addData('probold_slider.started', probold_slider.tStartRefresh)
thisExp.addData('probold_slider.stopped', probold_slider.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
thisExp.addData('instructions.started', instructions.tStartRefresh)
thisExp.addData('instructions.stopped', instructions.tStopRefresh)
# check responses
if key_resp_16.keys in ['', [], None]:  # No response was made
    key_resp_16.keys = None
thisExp.addData('key_resp_16.keys',key_resp_16.keys)
if key_resp_16.keys != None:  # we had a response
    thisExp.addData('key_resp_16.rt', key_resp_16.rt)
thisExp.nextEntry()
# the Routine "QuestionProb" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "QuestionCorrect"-------
continueRoutine = True
# update component parameters for each repeat
probcorrect_slider.reset()
# setup some python lists for storing info about the mouse_probcorrect
mouse_probcorrect.clicked_name = []
gotValidClick = False  # until a click is received
key_resp_18.keys = []
key_resp_18.rt = []
_key_resp_18_allKeys = []
# keep track of which components have finished
QuestionCorrectComponents = [correctq, probcorrect_slider, mouse_probcorrect, instructions_2, key_resp_18]
for thisComponent in QuestionCorrectComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
QuestionCorrectClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "QuestionCorrect"-------
while continueRoutine:
    # get current time
    t = QuestionCorrectClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=QuestionCorrectClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *correctq* updates
    if correctq.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        correctq.frameNStart = frameN  # exact frame index
        correctq.tStart = t  # local t and not account for scr refresh
        correctq.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(correctq, 'tStartRefresh')  # time at next scr refresh
        correctq.setAutoDraw(True)
    
    # *probcorrect_slider* updates
    if probcorrect_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        probcorrect_slider.frameNStart = frameN  # exact frame index
        probcorrect_slider.tStart = t  # local t and not account for scr refresh
        probcorrect_slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(probcorrect_slider, 'tStartRefresh')  # time at next scr refresh
        probcorrect_slider.setAutoDraw(True)
    
    # *instructions_2* updates
    if instructions_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_2.frameNStart = frameN  # exact frame index
        instructions_2.tStart = t  # local t and not account for scr refresh
        instructions_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_2, 'tStartRefresh')  # time at next scr refresh
        instructions_2.setAutoDraw(True)
    
    # *key_resp_18* updates
    waitOnFlip = False
    if key_resp_18.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
        # keep track of start time/frame for later
        key_resp_18.frameNStart = frameN  # exact frame index
        key_resp_18.tStart = t  # local t and not account for scr refresh
        key_resp_18.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_18, 'tStartRefresh')  # time at next scr refresh
        key_resp_18.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_18.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_18.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_18.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_18.getKeys(keyList=['c', 'C'], waitRelease=False)
        _key_resp_18_allKeys.extend(theseKeys)
        if len(_key_resp_18_allKeys):
            key_resp_18.keys = _key_resp_18_allKeys[-1].name  # just the last key pressed
            key_resp_18.rt = _key_resp_18_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in QuestionCorrectComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "QuestionCorrect"-------
for thisComponent in QuestionCorrectComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('correctq.started', correctq.tStartRefresh)
thisExp.addData('correctq.stopped', correctq.tStopRefresh)
thisExp.addData('probcorrect_slider.response', probcorrect_slider.getRating())
thisExp.addData('probcorrect_slider.rt', probcorrect_slider.getRT())
thisExp.addData('probcorrect_slider.started', probcorrect_slider.tStartRefresh)
thisExp.addData('probcorrect_slider.stopped', probcorrect_slider.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
# check responses
if key_resp_18.keys in ['', [], None]:  # No response was made
    key_resp_18.keys = None
thisExp.addData('key_resp_18.keys',key_resp_18.keys)
if key_resp_18.keys != None:  # we had a response
    thisExp.addData('key_resp_18.rt', key_resp_18.rt)
thisExp.nextEntry()
# the Routine "QuestionCorrect" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Question_SelfRank"-------
continueRoutine = True
# update component parameters for each repeat
selfrank_slider_s1.reset()
# setup some python lists for storing info about the mouse_selfrank
mouse_selfrank.clicked_name = []
gotValidClick = False  # until a click is received
key_resp_19.keys = []
key_resp_19.rt = []
_key_resp_19_allKeys = []
# keep track of which components have finished
Question_SelfRankComponents = [selfrankq, selfrank_slider_s1, mouse_selfrank, instructions_3, key_resp_19]
for thisComponent in Question_SelfRankComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Question_SelfRankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Question_SelfRank"-------
while continueRoutine:
    # get current time
    t = Question_SelfRankClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Question_SelfRankClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *selfrankq* updates
    if selfrankq.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        selfrankq.frameNStart = frameN  # exact frame index
        selfrankq.tStart = t  # local t and not account for scr refresh
        selfrankq.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(selfrankq, 'tStartRefresh')  # time at next scr refresh
        selfrankq.setAutoDraw(True)
    
    # *selfrank_slider_s1* updates
    if selfrank_slider_s1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        selfrank_slider_s1.frameNStart = frameN  # exact frame index
        selfrank_slider_s1.tStart = t  # local t and not account for scr refresh
        selfrank_slider_s1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(selfrank_slider_s1, 'tStartRefresh')  # time at next scr refresh
        selfrank_slider_s1.setAutoDraw(True)
    
    # *instructions_3* updates
    if instructions_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_3.frameNStart = frameN  # exact frame index
        instructions_3.tStart = t  # local t and not account for scr refresh
        instructions_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_3, 'tStartRefresh')  # time at next scr refresh
        instructions_3.setAutoDraw(True)
    
    # *key_resp_19* updates
    waitOnFlip = False
    if key_resp_19.status == NOT_STARTED and tThisFlip >= 0.3-frameTolerance:
        # keep track of start time/frame for later
        key_resp_19.frameNStart = frameN  # exact frame index
        key_resp_19.tStart = t  # local t and not account for scr refresh
        key_resp_19.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_19, 'tStartRefresh')  # time at next scr refresh
        key_resp_19.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_19.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_19.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_19.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_19.getKeys(keyList=['c', 'C'], waitRelease=False)
        _key_resp_19_allKeys.extend(theseKeys)
        if len(_key_resp_19_allKeys):
            key_resp_19.keys = _key_resp_19_allKeys[-1].name  # just the last key pressed
            key_resp_19.rt = _key_resp_19_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Question_SelfRankComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Question_SelfRank"-------
for thisComponent in Question_SelfRankComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('selfrank_slider_s1.response', selfrank_slider_s1.getRating())
thisExp.addData('selfrank_slider_s1.rt', selfrank_slider_s1.getRT())
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
# check responses
if key_resp_19.keys in ['', [], None]:  # No response was made
    key_resp_19.keys = None
thisExp.addData('key_resp_19.keys',key_resp_19.keys)
if key_resp_19.keys != None:  # we had a response
    thisExp.addData('key_resp_19.rt', key_resp_19.rt)
thisExp.nextEntry()
# the Routine "Question_SelfRank" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "QuestionHighConf"-------
continueRoutine = True
# update component parameters for each repeat
highconf_slider.reset()
# setup some python lists for storing info about the mouse_highconf
mouse_highconf.clicked_name = []
gotValidClick = False  # until a click is received
key_resp_17.keys = []
key_resp_17.rt = []
_key_resp_17_allKeys = []
# keep track of which components have finished
QuestionHighConfComponents = [highconfq, highconf_slider, mouse_highconf, instructions2, key_resp_17]
for thisComponent in QuestionHighConfComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
QuestionHighConfClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "QuestionHighConf"-------
while continueRoutine:
    # get current time
    t = QuestionHighConfClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=QuestionHighConfClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *highconfq* updates
    if highconfq.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        highconfq.frameNStart = frameN  # exact frame index
        highconfq.tStart = t  # local t and not account for scr refresh
        highconfq.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(highconfq, 'tStartRefresh')  # time at next scr refresh
        highconfq.setAutoDraw(True)
    
    # *highconf_slider* updates
    if highconf_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        highconf_slider.frameNStart = frameN  # exact frame index
        highconf_slider.tStart = t  # local t and not account for scr refresh
        highconf_slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(highconf_slider, 'tStartRefresh')  # time at next scr refresh
        highconf_slider.setAutoDraw(True)
    
    # *instructions2* updates
    if instructions2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions2.frameNStart = frameN  # exact frame index
        instructions2.tStart = t  # local t and not account for scr refresh
        instructions2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions2, 'tStartRefresh')  # time at next scr refresh
        instructions2.setAutoDraw(True)
    
    # *key_resp_17* updates
    waitOnFlip = False
    if key_resp_17.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
        # keep track of start time/frame for later
        key_resp_17.frameNStart = frameN  # exact frame index
        key_resp_17.tStart = t  # local t and not account for scr refresh
        key_resp_17.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_17, 'tStartRefresh')  # time at next scr refresh
        key_resp_17.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_17.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_17.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_17.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_17.getKeys(keyList=['c', 'C'], waitRelease=False)
        _key_resp_17_allKeys.extend(theseKeys)
        if len(_key_resp_17_allKeys):
            key_resp_17.keys = _key_resp_17_allKeys[-1].name  # just the last key pressed
            key_resp_17.rt = _key_resp_17_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in QuestionHighConfComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "QuestionHighConf"-------
for thisComponent in QuestionHighConfComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('highconfq.started', highconfq.tStartRefresh)
thisExp.addData('highconfq.stopped', highconfq.tStopRefresh)
thisExp.addData('highconf_slider.response', highconf_slider.getRating())
thisExp.addData('highconf_slider.rt', highconf_slider.getRT())
thisExp.addData('highconf_slider.started', highconf_slider.tStartRefresh)
thisExp.addData('highconf_slider.stopped', highconf_slider.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
thisExp.addData('instructions2.started', instructions2.tStartRefresh)
thisExp.addData('instructions2.stopped', instructions2.tStopRefresh)
# check responses
if key_resp_17.keys in ['', [], None]:  # No response was made
    key_resp_17.keys = None
thisExp.addData('key_resp_17.keys',key_resp_17.keys)
if key_resp_17.keys != None:  # we had a response
    thisExp.addData('key_resp_17.rt', key_resp_17.rt)
thisExp.nextEntry()
# the Routine "QuestionHighConf" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "QuestionLowConf"-------
continueRoutine = True
# update component parameters for each repeat
lowconf_slider.reset()
# setup some python lists for storing info about the mouse_lowconf
mouse_lowconf.clicked_name = []
gotValidClick = False  # until a click is received
key_resp_14.keys = []
key_resp_14.rt = []
_key_resp_14_allKeys = []
# keep track of which components have finished
QuestionLowConfComponents = [lowconfq, lowconf_slider, mouse_lowconf, instructions3, key_resp_14]
for thisComponent in QuestionLowConfComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
QuestionLowConfClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "QuestionLowConf"-------
while continueRoutine:
    # get current time
    t = QuestionLowConfClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=QuestionLowConfClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *lowconfq* updates
    if lowconfq.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        lowconfq.frameNStart = frameN  # exact frame index
        lowconfq.tStart = t  # local t and not account for scr refresh
        lowconfq.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(lowconfq, 'tStartRefresh')  # time at next scr refresh
        lowconfq.setAutoDraw(True)
    
    # *lowconf_slider* updates
    if lowconf_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        lowconf_slider.frameNStart = frameN  # exact frame index
        lowconf_slider.tStart = t  # local t and not account for scr refresh
        lowconf_slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(lowconf_slider, 'tStartRefresh')  # time at next scr refresh
        lowconf_slider.setAutoDraw(True)
    
    # *instructions3* updates
    if instructions3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions3.frameNStart = frameN  # exact frame index
        instructions3.tStart = t  # local t and not account for scr refresh
        instructions3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions3, 'tStartRefresh')  # time at next scr refresh
        instructions3.setAutoDraw(True)
    
    # *key_resp_14* updates
    waitOnFlip = False
    if key_resp_14.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
        # keep track of start time/frame for later
        key_resp_14.frameNStart = frameN  # exact frame index
        key_resp_14.tStart = t  # local t and not account for scr refresh
        key_resp_14.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_14, 'tStartRefresh')  # time at next scr refresh
        key_resp_14.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_14.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_14.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_14.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_14.getKeys(keyList=['c', 'C'], waitRelease=False)
        _key_resp_14_allKeys.extend(theseKeys)
        if len(_key_resp_14_allKeys):
            key_resp_14.keys = _key_resp_14_allKeys[-1].name  # just the last key pressed
            key_resp_14.rt = _key_resp_14_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in QuestionLowConfComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "QuestionLowConf"-------
for thisComponent in QuestionLowConfComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('lowconfq.started', lowconfq.tStartRefresh)
thisExp.addData('lowconfq.stopped', lowconfq.tStopRefresh)
thisExp.addData('lowconf_slider.response', lowconf_slider.getRating())
thisExp.addData('lowconf_slider.rt', lowconf_slider.getRT())
thisExp.addData('lowconf_slider.started', lowconf_slider.tStartRefresh)
thisExp.addData('lowconf_slider.stopped', lowconf_slider.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
thisExp.addData('instructions3.started', instructions3.tStartRefresh)
thisExp.addData('instructions3.stopped', instructions3.tStopRefresh)
# check responses
if key_resp_14.keys in ['', [], None]:  # No response was made
    key_resp_14.keys = None
thisExp.addData('key_resp_14.keys',key_resp_14.keys)
if key_resp_14.keys != None:  # we had a response
    thisExp.addData('key_resp_14.rt', key_resp_14.rt)
thisExp.nextEntry()
# the Routine "QuestionLowConf" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "QuestionMoneyScale"-------
continueRoutine = True
# update component parameters for each repeat
moneyscale_q1.reset()
# setup some python lists for storing info about the mouse_lowconf_2
mouse_lowconf_2.clicked_name = []
gotValidClick = False  # until a click is received
key_resp_23.keys = []
key_resp_23.rt = []
_key_resp_23_allKeys = []
# keep track of which components have finished
QuestionMoneyScaleComponents = [moneyscaleq1, moneyscale_q1, mouse_lowconf_2, instructions3_2, key_resp_23]
for thisComponent in QuestionMoneyScaleComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
QuestionMoneyScaleClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "QuestionMoneyScale"-------
while continueRoutine:
    # get current time
    t = QuestionMoneyScaleClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=QuestionMoneyScaleClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *moneyscaleq1* updates
    if moneyscaleq1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        moneyscaleq1.frameNStart = frameN  # exact frame index
        moneyscaleq1.tStart = t  # local t and not account for scr refresh
        moneyscaleq1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(moneyscaleq1, 'tStartRefresh')  # time at next scr refresh
        moneyscaleq1.setAutoDraw(True)
    
    # *moneyscale_q1* updates
    if moneyscale_q1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        moneyscale_q1.frameNStart = frameN  # exact frame index
        moneyscale_q1.tStart = t  # local t and not account for scr refresh
        moneyscale_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(moneyscale_q1, 'tStartRefresh')  # time at next scr refresh
        moneyscale_q1.setAutoDraw(True)
    
    # *instructions3_2* updates
    if instructions3_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions3_2.frameNStart = frameN  # exact frame index
        instructions3_2.tStart = t  # local t and not account for scr refresh
        instructions3_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions3_2, 'tStartRefresh')  # time at next scr refresh
        instructions3_2.setAutoDraw(True)
    
    # *key_resp_23* updates
    waitOnFlip = False
    if key_resp_23.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
        # keep track of start time/frame for later
        key_resp_23.frameNStart = frameN  # exact frame index
        key_resp_23.tStart = t  # local t and not account for scr refresh
        key_resp_23.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_23, 'tStartRefresh')  # time at next scr refresh
        key_resp_23.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_23.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_23.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_23.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_23.getKeys(keyList=['c', 'C'], waitRelease=False)
        _key_resp_23_allKeys.extend(theseKeys)
        if len(_key_resp_23_allKeys):
            key_resp_23.keys = _key_resp_23_allKeys[-1].name  # just the last key pressed
            key_resp_23.rt = _key_resp_23_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in QuestionMoneyScaleComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "QuestionMoneyScale"-------
for thisComponent in QuestionMoneyScaleComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('moneyscaleq1.started', moneyscaleq1.tStartRefresh)
thisExp.addData('moneyscaleq1.stopped', moneyscaleq1.tStopRefresh)
thisExp.addData('moneyscale_q1.response', moneyscale_q1.getRating())
thisExp.addData('moneyscale_q1.rt', moneyscale_q1.getRT())
thisExp.addData('moneyscale_q1.started', moneyscale_q1.tStartRefresh)
thisExp.addData('moneyscale_q1.stopped', moneyscale_q1.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
thisExp.addData('instructions3_2.started', instructions3_2.tStartRefresh)
thisExp.addData('instructions3_2.stopped', instructions3_2.tStopRefresh)
# check responses
if key_resp_23.keys in ['', [], None]:  # No response was made
    key_resp_23.keys = None
thisExp.addData('key_resp_23.keys',key_resp_23.keys)
if key_resp_23.keys != None:  # we had a response
    thisExp.addData('key_resp_23.rt', key_resp_23.rt)
thisExp.nextEntry()
# the Routine "QuestionMoneyScale" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "QuestionMemoryScale"-------
continueRoutine = True
# update component parameters for each repeat
memoryscale_q1.reset()
# setup some python lists for storing info about the mouse_lowconf_3
mouse_lowconf_3.clicked_name = []
gotValidClick = False  # until a click is received
key_resp_24.keys = []
key_resp_24.rt = []
_key_resp_24_allKeys = []
# keep track of which components have finished
QuestionMemoryScaleComponents = [memoryscaleq1, memoryscale_q1, mouse_lowconf_3, instructions3_3, key_resp_24]
for thisComponent in QuestionMemoryScaleComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
QuestionMemoryScaleClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "QuestionMemoryScale"-------
while continueRoutine:
    # get current time
    t = QuestionMemoryScaleClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=QuestionMemoryScaleClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *memoryscaleq1* updates
    if memoryscaleq1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        memoryscaleq1.frameNStart = frameN  # exact frame index
        memoryscaleq1.tStart = t  # local t and not account for scr refresh
        memoryscaleq1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(memoryscaleq1, 'tStartRefresh')  # time at next scr refresh
        memoryscaleq1.setAutoDraw(True)
    
    # *memoryscale_q1* updates
    if memoryscale_q1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        memoryscale_q1.frameNStart = frameN  # exact frame index
        memoryscale_q1.tStart = t  # local t and not account for scr refresh
        memoryscale_q1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(memoryscale_q1, 'tStartRefresh')  # time at next scr refresh
        memoryscale_q1.setAutoDraw(True)
    
    # *instructions3_3* updates
    if instructions3_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions3_3.frameNStart = frameN  # exact frame index
        instructions3_3.tStart = t  # local t and not account for scr refresh
        instructions3_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions3_3, 'tStartRefresh')  # time at next scr refresh
        instructions3_3.setAutoDraw(True)
    
    # *key_resp_24* updates
    waitOnFlip = False
    if key_resp_24.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
        # keep track of start time/frame for later
        key_resp_24.frameNStart = frameN  # exact frame index
        key_resp_24.tStart = t  # local t and not account for scr refresh
        key_resp_24.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_24, 'tStartRefresh')  # time at next scr refresh
        key_resp_24.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_24.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_24.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_24.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_24.getKeys(keyList=['c', 'C'], waitRelease=False)
        _key_resp_24_allKeys.extend(theseKeys)
        if len(_key_resp_24_allKeys):
            key_resp_24.keys = _key_resp_24_allKeys[-1].name  # just the last key pressed
            key_resp_24.rt = _key_resp_24_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in QuestionMemoryScaleComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "QuestionMemoryScale"-------
for thisComponent in QuestionMemoryScaleComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('memoryscaleq1.started', memoryscaleq1.tStartRefresh)
thisExp.addData('memoryscaleq1.stopped', memoryscaleq1.tStopRefresh)
thisExp.addData('memoryscale_q1.response', memoryscale_q1.getRating())
thisExp.addData('memoryscale_q1.rt', memoryscale_q1.getRT())
thisExp.addData('memoryscale_q1.started', memoryscale_q1.tStartRefresh)
thisExp.addData('memoryscale_q1.stopped', memoryscale_q1.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
thisExp.addData('instructions3_3.started', instructions3_3.tStartRefresh)
thisExp.addData('instructions3_3.stopped', instructions3_3.tStopRefresh)
# check responses
if key_resp_24.keys in ['', [], None]:  # No response was made
    key_resp_24.keys = None
thisExp.addData('key_resp_24.keys',key_resp_24.keys)
if key_resp_24.keys != None:  # we had a response
    thisExp.addData('key_resp_24.rt', key_resp_24.rt)
thisExp.nextEntry()
# the Routine "QuestionMemoryScale" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "UncertaintyMoneyScale"-------
continueRoutine = True
# update component parameters for each repeat
uncertainty_money_q_response.reset()
# setup some python lists for storing info about the mouse_lowconf_4
mouse_lowconf_4.clicked_name = []
gotValidClick = False  # until a click is received
key_resp_25.keys = []
key_resp_25.rt = []
_key_resp_25_allKeys = []
# keep track of which components have finished
UncertaintyMoneyScaleComponents = [uncertainty_money_q, uncertainty_money_q_response, mouse_lowconf_4, instructions3_4, key_resp_25]
for thisComponent in UncertaintyMoneyScaleComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
UncertaintyMoneyScaleClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "UncertaintyMoneyScale"-------
while continueRoutine:
    # get current time
    t = UncertaintyMoneyScaleClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=UncertaintyMoneyScaleClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *uncertainty_money_q* updates
    if uncertainty_money_q.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        uncertainty_money_q.frameNStart = frameN  # exact frame index
        uncertainty_money_q.tStart = t  # local t and not account for scr refresh
        uncertainty_money_q.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(uncertainty_money_q, 'tStartRefresh')  # time at next scr refresh
        uncertainty_money_q.setAutoDraw(True)
    
    # *uncertainty_money_q_response* updates
    if uncertainty_money_q_response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        uncertainty_money_q_response.frameNStart = frameN  # exact frame index
        uncertainty_money_q_response.tStart = t  # local t and not account for scr refresh
        uncertainty_money_q_response.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(uncertainty_money_q_response, 'tStartRefresh')  # time at next scr refresh
        uncertainty_money_q_response.setAutoDraw(True)
    
    # *instructions3_4* updates
    if instructions3_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions3_4.frameNStart = frameN  # exact frame index
        instructions3_4.tStart = t  # local t and not account for scr refresh
        instructions3_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions3_4, 'tStartRefresh')  # time at next scr refresh
        instructions3_4.setAutoDraw(True)
    
    # *key_resp_25* updates
    waitOnFlip = False
    if key_resp_25.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
        # keep track of start time/frame for later
        key_resp_25.frameNStart = frameN  # exact frame index
        key_resp_25.tStart = t  # local t and not account for scr refresh
        key_resp_25.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_25, 'tStartRefresh')  # time at next scr refresh
        key_resp_25.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_25.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_25.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_25.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_25.getKeys(keyList=['c', 'C'], waitRelease=False)
        _key_resp_25_allKeys.extend(theseKeys)
        if len(_key_resp_25_allKeys):
            key_resp_25.keys = _key_resp_25_allKeys[-1].name  # just the last key pressed
            key_resp_25.rt = _key_resp_25_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in UncertaintyMoneyScaleComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "UncertaintyMoneyScale"-------
for thisComponent in UncertaintyMoneyScaleComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('uncertainty_money_q.started', uncertainty_money_q.tStartRefresh)
thisExp.addData('uncertainty_money_q.stopped', uncertainty_money_q.tStopRefresh)
thisExp.addData('uncertainty_money_q_response.response', uncertainty_money_q_response.getRating())
thisExp.addData('uncertainty_money_q_response.rt', uncertainty_money_q_response.getRT())
thisExp.addData('uncertainty_money_q_response.started', uncertainty_money_q_response.tStartRefresh)
thisExp.addData('uncertainty_money_q_response.stopped', uncertainty_money_q_response.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
thisExp.addData('instructions3_4.started', instructions3_4.tStartRefresh)
thisExp.addData('instructions3_4.stopped', instructions3_4.tStopRefresh)
# check responses
if key_resp_25.keys in ['', [], None]:  # No response was made
    key_resp_25.keys = None
thisExp.addData('key_resp_25.keys',key_resp_25.keys)
if key_resp_25.keys != None:  # we had a response
    thisExp.addData('key_resp_25.rt', key_resp_25.rt)
thisExp.nextEntry()
# the Routine "UncertaintyMoneyScale" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "UncertaintyMemoryScale"-------
continueRoutine = True
# update component parameters for each repeat
uncertainty_memory_q_response.reset()
# setup some python lists for storing info about the mouse_lowconf_5
mouse_lowconf_5.clicked_name = []
gotValidClick = False  # until a click is received
key_resp_26.keys = []
key_resp_26.rt = []
_key_resp_26_allKeys = []
# keep track of which components have finished
UncertaintyMemoryScaleComponents = [uncertainty_memory_q, uncertainty_memory_q_response, mouse_lowconf_5, instructions3_5, key_resp_26]
for thisComponent in UncertaintyMemoryScaleComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
UncertaintyMemoryScaleClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "UncertaintyMemoryScale"-------
while continueRoutine:
    # get current time
    t = UncertaintyMemoryScaleClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=UncertaintyMemoryScaleClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *uncertainty_memory_q* updates
    if uncertainty_memory_q.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        uncertainty_memory_q.frameNStart = frameN  # exact frame index
        uncertainty_memory_q.tStart = t  # local t and not account for scr refresh
        uncertainty_memory_q.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(uncertainty_memory_q, 'tStartRefresh')  # time at next scr refresh
        uncertainty_memory_q.setAutoDraw(True)
    
    # *uncertainty_memory_q_response* updates
    if uncertainty_memory_q_response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        uncertainty_memory_q_response.frameNStart = frameN  # exact frame index
        uncertainty_memory_q_response.tStart = t  # local t and not account for scr refresh
        uncertainty_memory_q_response.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(uncertainty_memory_q_response, 'tStartRefresh')  # time at next scr refresh
        uncertainty_memory_q_response.setAutoDraw(True)
    
    # *instructions3_5* updates
    if instructions3_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions3_5.frameNStart = frameN  # exact frame index
        instructions3_5.tStart = t  # local t and not account for scr refresh
        instructions3_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions3_5, 'tStartRefresh')  # time at next scr refresh
        instructions3_5.setAutoDraw(True)
    
    # *key_resp_26* updates
    waitOnFlip = False
    if key_resp_26.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
        # keep track of start time/frame for later
        key_resp_26.frameNStart = frameN  # exact frame index
        key_resp_26.tStart = t  # local t and not account for scr refresh
        key_resp_26.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_26, 'tStartRefresh')  # time at next scr refresh
        key_resp_26.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_26.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_26.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_26.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_26.getKeys(keyList=['c', 'C'], waitRelease=False)
        _key_resp_26_allKeys.extend(theseKeys)
        if len(_key_resp_26_allKeys):
            key_resp_26.keys = _key_resp_26_allKeys[-1].name  # just the last key pressed
            key_resp_26.rt = _key_resp_26_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in UncertaintyMemoryScaleComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "UncertaintyMemoryScale"-------
for thisComponent in UncertaintyMemoryScaleComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('uncertainty_memory_q.started', uncertainty_memory_q.tStartRefresh)
thisExp.addData('uncertainty_memory_q.stopped', uncertainty_memory_q.tStopRefresh)
thisExp.addData('uncertainty_memory_q_response.response', uncertainty_memory_q_response.getRating())
thisExp.addData('uncertainty_memory_q_response.rt', uncertainty_memory_q_response.getRT())
thisExp.addData('uncertainty_memory_q_response.started', uncertainty_memory_q_response.tStartRefresh)
thisExp.addData('uncertainty_memory_q_response.stopped', uncertainty_memory_q_response.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
thisExp.addData('instructions3_5.started', instructions3_5.tStartRefresh)
thisExp.addData('instructions3_5.stopped', instructions3_5.tStopRefresh)
# check responses
if key_resp_26.keys in ['', [], None]:  # No response was made
    key_resp_26.keys = None
thisExp.addData('key_resp_26.keys',key_resp_26.keys)
if key_resp_26.keys != None:  # we had a response
    thisExp.addData('key_resp_26.rt', key_resp_26.rt)
thisExp.nextEntry()
# the Routine "UncertaintyMemoryScale" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Memory_or_Money_Binary"-------
continueRoutine = True
# update component parameters for each repeat
mem_or_money_binary_response.reset()
# setup some python lists for storing info about the mouse_lowconf_6
mouse_lowconf_6.clicked_name = []
gotValidClick = False  # until a click is received
key_resp_27.keys = []
key_resp_27.rt = []
_key_resp_27_allKeys = []
# keep track of which components have finished
Memory_or_Money_BinaryComponents = [mem_or_money_q, mem_or_money_binary_response, mouse_lowconf_6, instructions3_6, key_resp_27]
for thisComponent in Memory_or_Money_BinaryComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Memory_or_Money_BinaryClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Memory_or_Money_Binary"-------
while continueRoutine:
    # get current time
    t = Memory_or_Money_BinaryClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Memory_or_Money_BinaryClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *mem_or_money_q* updates
    if mem_or_money_q.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mem_or_money_q.frameNStart = frameN  # exact frame index
        mem_or_money_q.tStart = t  # local t and not account for scr refresh
        mem_or_money_q.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mem_or_money_q, 'tStartRefresh')  # time at next scr refresh
        mem_or_money_q.setAutoDraw(True)
    
    # *mem_or_money_binary_response* updates
    if mem_or_money_binary_response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mem_or_money_binary_response.frameNStart = frameN  # exact frame index
        mem_or_money_binary_response.tStart = t  # local t and not account for scr refresh
        mem_or_money_binary_response.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mem_or_money_binary_response, 'tStartRefresh')  # time at next scr refresh
        mem_or_money_binary_response.setAutoDraw(True)
    
    # *instructions3_6* updates
    if instructions3_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions3_6.frameNStart = frameN  # exact frame index
        instructions3_6.tStart = t  # local t and not account for scr refresh
        instructions3_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions3_6, 'tStartRefresh')  # time at next scr refresh
        instructions3_6.setAutoDraw(True)
    
    # *key_resp_27* updates
    waitOnFlip = False
    if key_resp_27.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
        # keep track of start time/frame for later
        key_resp_27.frameNStart = frameN  # exact frame index
        key_resp_27.tStart = t  # local t and not account for scr refresh
        key_resp_27.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_27, 'tStartRefresh')  # time at next scr refresh
        key_resp_27.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_27.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_27.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_27.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_27.getKeys(keyList=['c', 'C'], waitRelease=False)
        _key_resp_27_allKeys.extend(theseKeys)
        if len(_key_resp_27_allKeys):
            key_resp_27.keys = _key_resp_27_allKeys[-1].name  # just the last key pressed
            key_resp_27.rt = _key_resp_27_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Memory_or_Money_BinaryComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Memory_or_Money_Binary"-------
for thisComponent in Memory_or_Money_BinaryComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('mem_or_money_q.started', mem_or_money_q.tStartRefresh)
thisExp.addData('mem_or_money_q.stopped', mem_or_money_q.tStopRefresh)
thisExp.addData('mem_or_money_binary_response.response', mem_or_money_binary_response.getRating())
thisExp.addData('mem_or_money_binary_response.rt', mem_or_money_binary_response.getRT())
thisExp.addData('mem_or_money_binary_response.started', mem_or_money_binary_response.tStartRefresh)
thisExp.addData('mem_or_money_binary_response.stopped', mem_or_money_binary_response.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
thisExp.addData('instructions3_6.started', instructions3_6.tStartRefresh)
thisExp.addData('instructions3_6.stopped', instructions3_6.tStopRefresh)
# check responses
if key_resp_27.keys in ['', [], None]:  # No response was made
    key_resp_27.keys = None
thisExp.addData('key_resp_27.keys',key_resp_27.keys)
if key_resp_27.keys != None:  # we had a response
    thisExp.addData('key_resp_27.rt', key_resp_27.rt)
thisExp.nextEntry()
# the Routine "Memory_or_Money_Binary" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Blank100"-------
continueRoutine = True
routineTimer.add(0.100000)
# update component parameters for each repeat
# keep track of which components have finished
Blank100Components = [Blank_2]
for thisComponent in Blank100Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Blank100Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Blank100"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Blank100Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Blank100Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Blank_2* updates
    if Blank_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Blank_2.frameNStart = frameN  # exact frame index
        Blank_2.tStart = t  # local t and not account for scr refresh
        Blank_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Blank_2, 'tStartRefresh')  # time at next scr refresh
        Blank_2.setAutoDraw(True)
    if Blank_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Blank_2.tStartRefresh + 0.1-frameTolerance:
            # keep track of stop time/frame for later
            Blank_2.tStop = t  # not accounting for scr refresh
            Blank_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Blank_2, 'tStopRefresh')  # time at next scr refresh
            Blank_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Blank100Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Blank100"-------
for thisComponent in Blank100Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Blank_2.started', Blank_2.tStartRefresh)
thisExp.addData('Blank_2.stopped', Blank_2.tStopRefresh)

# ------Prepare to start Routine "FreeResponse_2"-------
continueRoutine = True
# update component parameters for each repeat
comments.reset()
# setup some python lists for storing info about the mouse
mouse.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
FreeResponse_2Components = [Question_2, comments, mouse, Clickable_2]
for thisComponent in FreeResponse_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
FreeResponse_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "FreeResponse_2"-------
while continueRoutine:
    # get current time
    t = FreeResponse_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=FreeResponse_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Question_2* updates
    if Question_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Question_2.frameNStart = frameN  # exact frame index
        Question_2.tStart = t  # local t and not account for scr refresh
        Question_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Question_2, 'tStartRefresh')  # time at next scr refresh
        Question_2.setAutoDraw(True)
    
    # *comments* updates
    if comments.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        comments.frameNStart = frameN  # exact frame index
        comments.tStart = t  # local t and not account for scr refresh
        comments.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(comments, 'tStartRefresh')  # time at next scr refresh
        comments.setAutoDraw(True)
    # *mouse* updates
    if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse.frameNStart = frameN  # exact frame index
        mouse.tStart = t  # local t and not account for scr refresh
        mouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
        mouse.status = STARTED
        mouse.mouseClock.reset()
        prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
    if mouse.status == STARTED:  # only update if started and not finished!
        buttons = mouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(Clickable_2)
                    clickableList = Clickable_2
                except:
                    clickableList = [Clickable_2]
                for obj in clickableList:
                    if obj.contains(mouse):
                        gotValidClick = True
                        mouse.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # *Clickable_2* updates
    if Clickable_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Clickable_2.frameNStart = frameN  # exact frame index
        Clickable_2.tStart = t  # local t and not account for scr refresh
        Clickable_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Clickable_2, 'tStartRefresh')  # time at next scr refresh
        Clickable_2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in FreeResponse_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "FreeResponse_2"-------
for thisComponent in FreeResponse_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Question_2.started', Question_2.tStartRefresh)
thisExp.addData('Question_2.stopped', Question_2.tStopRefresh)
thisExp.addData('comments.text',comments.text)
thisExp.addData('comments.started', comments.tStartRefresh)
thisExp.addData('comments.stopped', comments.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
thisExp.addData('Clickable_2.started', Clickable_2.tStartRefresh)
thisExp.addData('Clickable_2.stopped', Clickable_2.tStopRefresh)
# the Routine "FreeResponse_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "FinishScreen"-------
continueRoutine = True
# update component parameters for each repeat
experimentearning.setText(exptotal_earning)
key_resp_20.keys = []
key_resp_20.rt = []
_key_resp_20_allKeys = []
# keep track of which components have finished
FinishScreenComponents = [thankyoumsg_2, experimentearning, key_resp_20, text_6]
for thisComponent in FinishScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
FinishScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "FinishScreen"-------
while continueRoutine:
    # get current time
    t = FinishScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=FinishScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thankyoumsg_2* updates
    if thankyoumsg_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        thankyoumsg_2.frameNStart = frameN  # exact frame index
        thankyoumsg_2.tStart = t  # local t and not account for scr refresh
        thankyoumsg_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thankyoumsg_2, 'tStartRefresh')  # time at next scr refresh
        thankyoumsg_2.setAutoDraw(True)
    
    # *experimentearning* updates
    if experimentearning.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        experimentearning.frameNStart = frameN  # exact frame index
        experimentearning.tStart = t  # local t and not account for scr refresh
        experimentearning.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(experimentearning, 'tStartRefresh')  # time at next scr refresh
        experimentearning.setAutoDraw(True)
    
    # *key_resp_20* updates
    waitOnFlip = False
    if key_resp_20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_20.frameNStart = frameN  # exact frame index
        key_resp_20.tStart = t  # local t and not account for scr refresh
        key_resp_20.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_20, 'tStartRefresh')  # time at next scr refresh
        key_resp_20.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_20.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_20.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_20.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_20.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_20_allKeys.extend(theseKeys)
        if len(_key_resp_20_allKeys):
            key_resp_20.keys = _key_resp_20_allKeys[-1].name  # just the last key pressed
            key_resp_20.rt = _key_resp_20_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_6* updates
    if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_6.frameNStart = frameN  # exact frame index
        text_6.tStart = t  # local t and not account for scr refresh
        text_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
        text_6.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in FinishScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "FinishScreen"-------
for thisComponent in FinishScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('thankyoumsg_2.started', thankyoumsg_2.tStartRefresh)
thisExp.addData('thankyoumsg_2.stopped', thankyoumsg_2.tStopRefresh)
thisExp.addData('experimentearning.started', experimentearning.tStartRefresh)
thisExp.addData('experimentearning.stopped', experimentearning.tStopRefresh)
# check responses
if key_resp_20.keys in ['', [], None]:  # No response was made
    key_resp_20.keys = None
thisExp.addData('key_resp_20.keys',key_resp_20.keys)
if key_resp_20.keys != None:  # we had a response
    thisExp.addData('key_resp_20.rt', key_resp_20.rt)
thisExp.addData('key_resp_20.started', key_resp_20.tStartRefresh)
thisExp.addData('key_resp_20.stopped', key_resp_20.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('text_6.started', text_6.tStartRefresh)
thisExp.addData('text_6.stopped', text_6.tStopRefresh)
# the Routine "FinishScreen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "EndMessage"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_final.keys = []
key_resp_final.rt = []
_key_resp_final_allKeys = []
# keep track of which components have finished
EndMessageComponents = [thankyoumsg, key_resp_final]
for thisComponent in EndMessageComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndMessageClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "EndMessage"-------
while continueRoutine:
    # get current time
    t = EndMessageClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndMessageClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thankyoumsg* updates
    if thankyoumsg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        thankyoumsg.frameNStart = frameN  # exact frame index
        thankyoumsg.tStart = t  # local t and not account for scr refresh
        thankyoumsg.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thankyoumsg, 'tStartRefresh')  # time at next scr refresh
        thankyoumsg.setAutoDraw(True)
    
    # *key_resp_final* updates
    waitOnFlip = False
    if key_resp_final.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_final.frameNStart = frameN  # exact frame index
        key_resp_final.tStart = t  # local t and not account for scr refresh
        key_resp_final.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_final, 'tStartRefresh')  # time at next scr refresh
        key_resp_final.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_final.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_final.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_final.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_final.getKeys(keyList=['space', 'e', 'E', 'esc'], waitRelease=False)
        _key_resp_final_allKeys.extend(theseKeys)
        if len(_key_resp_final_allKeys):
            key_resp_final.keys = _key_resp_final_allKeys[-1].name  # just the last key pressed
            key_resp_final.rt = _key_resp_final_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndMessageComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "EndMessage"-------
for thisComponent in EndMessageComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('thankyoumsg.started', thankyoumsg.tStartRefresh)
thisExp.addData('thankyoumsg.stopped', thankyoumsg.tStopRefresh)
# check responses
if key_resp_final.keys in ['', [], None]:  # No response was made
    key_resp_final.keys = None
thisExp.addData('key_resp_final.keys',key_resp_final.keys)
if key_resp_final.keys != None:  # we had a response
    thisExp.addData('key_resp_final.rt', key_resp_final.rt)
thisExp.addData('key_resp_final.started', key_resp_final.tStartRefresh)
thisExp.addData('key_resp_final.stopped', key_resp_final.tStopRefresh)
thisExp.nextEntry()
# the Routine "EndMessage" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
