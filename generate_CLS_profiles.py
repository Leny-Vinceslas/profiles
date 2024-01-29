#AUTHOR: LENY VINCESLAS 
#%%
from itertools import permutations
import random




def generate_text_file(name, file_id,fileName,remark):
    template = f"""MeasurementProfile: {{
  ID: \\{{{file_id}\\}}
  CONFIGFILE: $\{{~kls\}}/etc/kls.cfg
  TARGETFILE: $\{{~kls\}}/etc\\\\\\{{{file_id}\\}}.hd
  KeyWords: headphone editable
  DbcLastChange: 2023 12 1 11 17 15 57 0784
  Name: "{name}"
  Remark: "{remark}dB Max level"
}}
TargetFile: {{
  # id 65edecc8a602be0a1f83748e34c58cc9706266
  # version 2.3.1.202
  # file ${{~kls}}/etc\\{{{file_id}\\}}.hd
  Signals: {{
    QueryGroupSignals: {{
      search signal header $\\{{DestinationHeader\\}} where 'SignalInfo/GroupId contains thirdoctave_lnn_kls_1'
    }}
    QuerySingleSignals: {{
      search signal header $\\{{DestinationHeader\\}} where 'SignalInfo/Keywords contains noise'
    }}
  }}
  TransducerType: headphone
  LevelControl: Adaptive
  LevelUnit: SPL
  SignalGroup: _KLS_SIGNALS_SINGLE_
  DefaultType: left/right
  R&D: 0
  Scripts: {{
    TargetSetup: {{
    }}
  }}
  GroupShuffle: none
  BlockShuffle: user
  MeasurementId: KLS
  InterStimulusPause: 500
  NonAdaptiveMinLevel: 10
  NonAdaptiveMaxLevel: 100
  NonAdaptiveIntervals: 9
  NonAdaptiveRepetitions: 1
  ClientLanguage: eng
  BlockGroups: {{
    {block_parameters}
  }}
  ConfigFile: $\\{{~kls\\}}/etc/kls.cfg
  editable: 1
  ReferenceDataVersion: 1
  Scale: {{
    50: extremely loud
    45: very loud
    40: $WEDGE 0.8 0.7
    35: loud
    30: $WEDGE 0.6 0.5
    25: medium
    20: $WEDGE 0.4 0.3
    15: soft
    10: $WEDGE 0.2 0.1
    5: very soft
    0: not heard
  }}
  ScaleString: \\"extremely loud test\\" \\"very loud\\" \\"$WEDGE 0.8 0.7\\" loud \\"$WEDGE 0.6 0.5\\" medium \\"$WEDGE 0.4 0.3\\" soft \\"$WEDGE 0.2 0.1\\" \\"very soft\\" \\"not heard\\"
  FitControl: LinBez2x3C
}}
"""

    with open(fileName, 'w') as file:
        file.write(template)      

def repetitionStruct(nBlocks,nReps):
    
    combinations=[]
    digits = list(range(nBlocks))
    # for permutation in permutations(digits,4):
    #   combinations.append(permutation)
    combinations=list(permutations(digits,nBlocks))
    reps=list(permutations(range(len(combinations)),nReps))

    return combinations, reps
  

def generate_random_id():
    # Define the format of the ID
    format_lengths = [8, 4, 4, 4, 12]

    # Function to generate a random string of given length
    def generate_random_string(length):
        characters = '0123456789ABCDEF'
        return ''.join(random.choice(characters) for _ in range(length))

    # Generate random strings for each segment
    id_segments = [generate_random_string(length) for length in format_lengths]

    # Join the segments with hyphens to form the final ID
    random_id = '-'.join(id_segments)

    return random_id
        

#%% ----------------------------------- Script beginning  here ------------------------------

nReps=3
# trains, blocks = defineABCD()

AdaptiveMaxLevels= list(range(60,100,5))
nFile=len(AdaptiveMaxLevels)

for count, AdaptiveMaxLevel in  enumerate(AdaptiveMaxLevels): 

  #Define Rep structure
  rdmID_train=generate_random_id()
  block_parameters = ""
  #Implement channel 0 and -0 for trains and blocks when i is odd or even
  # parameter AdaptiveMaxLevel going from 95db to 60db
   
  block_parameters += f"""{{
      GroupId: \\{{{rdmID_train}\\}}
      SignalGroup: _KLS_SIGNALS_SINGLE_
      LevelUnit: SPL
      ChannelLevels: 0
      SignalGroupDisplayName: Single signals
      Blocks: {{
        {{
          Signal: id engmatrixnoise
          Enabled: 1
          AdaptiveMaxLevel: {AdaptiveMaxLevel}
          CalibrationReference: engmatrixnoise
          Repetitions: 0
          SignalLength: 1000
          RampLength: 50
          LevelOffset: 0
          TrialsTotal: 20
          SignalDisplayName: Noise English (UK) Matrix Test
        }}
      }}
    }}
    {{
      GroupId: \\{{{rdmID_train}\\}}
      SignalGroup: _KLS_SIGNALS_SINGLE_
      LevelUnit: SPL
      ChannelLevels: - 0
      SignalGroupDisplayName: Single signals
      Blocks: {{
        {{
          Signal: id engmatrixnoise
          Enabled: 1
          AdaptiveMaxLevel: {AdaptiveMaxLevel}
          CalibrationReference: engmatrixnoise
          Repetitions: 0
          SignalLength: 1000
          RampLength: 50
          LevelOffset: 0
          TrialsTotal: 20
          SignalDisplayName: Noise English (UK) Matrix Test
        }}
      }}
    }}
    """
  
  for rep  in range(nReps):  
    rdmID_block=generate_random_id()
    block_parameters += f"""  {{
      GroupId: \\{{{rdmID_block}\\}}
      SignalGroup: _KLS_SIGNALS_SINGLE_
      LevelUnit: SPL
      ChannelLevels: 0
      SignalGroupDisplayName: Single signals
      Blocks: {{
        {{
          Signal: id engmatrixnoise
          Enabled: 1
          AdaptiveMaxLevel: {AdaptiveMaxLevel}
          CalibrationReference: engmatrixnoise
          Repetitions: 0
          SignalLength: 1000
          RampLength: 50
          LevelOffset: 0
          TrialsTotal: 20
          SignalDisplayName: Noise English (UK) Matrix Test
        }}
      }}
    }}
    {{
      GroupId: \\{{{rdmID_block}\\}}
      SignalGroup: _KLS_SIGNALS_SINGLE_
      LevelUnit: SPL
      ChannelLevels: - 0
      SignalGroupDisplayName: Single signals
      Blocks: {{
        {{
          Signal: id engmatrixnoise
          Enabled: 1
          AdaptiveMaxLevel: {AdaptiveMaxLevel}
          CalibrationReference: engmatrixnoise
          Repetitions: 0
          SignalLength: 1000
          RampLength: 50
          LevelOffset: 0
          TrialsTotal: 20
          SignalDisplayName: Noise English (UK) Matrix Test
        }}
      }}
    }}
  """
  name = "mainClsProfile_TAAA"+str(nReps)+'reps_ULL'+str(AdaptiveMaxLevel)+'dB'
  file_id = generate_random_id()
  fileName='CLS_profiles\mainClsProfile_TAAA'+str(nReps)+'reps_ULL'+str(AdaptiveMaxLevel)+'dB'+'.txt'
  generate_text_file(name, file_id, fileName,remark=AdaptiveMaxLevel)

# %%
