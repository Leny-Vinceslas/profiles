#AUTHOR: LENY VINCESLAS 
#%%
from itertools import permutations
import random
from defineBlocks_matrix import defineABCD 
from defineBlocks_matrix import defineABCSlope 


def generate_text_file(name, file_id, block_parameters,fileName):
    template = f"""MeasurementProfile: {{
  ID: \\{{{file_id}\\}}
  CONFIGFILE: ${{~engmatrix}}/etc/engmatrix.cfg
  TARGETFILE: ${{~engmatrix}}/etc\\\\\\{{{file_id}\\}}.hd
  KeyWords: headphone editable
  DbcLastChange: 2024 01 1 22 16 34 08 0830
  Name: "{name}"
}}
TargetFile: {{
  # id 65b3707dd7a0de07c71d564844544b83e86f54
  # version 2.6.0.203
  # file ${{~engmatrix}}/etc\\{{{file_id}\\}}.hd
  TransducerType: headphone
  LevelControl: OldenburgerLX 0.5
  FitControl: OldenburgerLX 0.5
  BlockGroups: {{
    {{ # BlockGroups 0
      Blocks: {{
{block_parameters}
      }}
    }}
  }}
  R&D: 0
  Scripts: {{
    TargetSetup: {{
    }}
  }}
  GroupShuffle: none
  BlockShuffle: none
  TrialShuffle: full
  StoreMode: Block
  MeasurementId: ENGMatrix
  ClientLanguage: eng
  CalibrationReference: engmatrixnoise
  ClosedResponse: 0
  LevelUnit: HL
  OriginalNoise: id engmatrixnoise
  MaskingNoise: id engmatrixnoise
  AllowConvolutions: 1
  InitOptionsHeader: {{
  }}
  TestListStartQuery: 1
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
nFiles=10
nReps=3
# trains, blocks = defineABCD()
trains, blocks = defineABCSlope()
combinations,reps=repetitionStruct(len(blocks),nReps)
nCombinations=len(combinations)
fileStructs=random.sample(reps,nFiles)

for count, fileStruct in  enumerate(fileStructs): 

  #Define Rep structure

  block_parameters = ""
  for i in range(len(trains)): 
      block_parameters += f"""       {{
          Noise: id engmatrixnoise
          SpeechLevel: {trains[i]['speechlevel']}
          SNR: {trains[i]['snr']}
          AudiometerCalibrationReference: engmatrixnoise
          LevelControl: {trains[i]['level_control']}
          FitControl: {trains[i]['fit_control']}
          LevelControl_Selected: {trains[i]['level_control_selected']}
          FitControl_Selected: {trains[i]['fit_control_selected']}
          NoiseChannelLevels: {trains[i]['noise_channel_levels']}
          SpeechChannelLevels: {trains[i]['speech_channel_levels']}
          TestListDefaultSubHeader: {trains[i]['testlist_default_subheader']}
         }}
  """
  
  for k, repID  in enumerate(fileStruct):  
    for j, blockID  in enumerate(combinations[repID]): 
        block_parameters += f"""       {{
          Noise: id engmatrixnoise
          SpeechLevel: {blocks[blockID]['speechlevel']}
          SNR: {blocks[blockID]['snr']}
          AudiometerCalibrationReference: engmatrixnoise
          LevelControl: {blocks[blockID]['level_control']}
          FitControl: {blocks[blockID]['fit_control']}
          LevelControl_Selected: {blocks[blockID]['level_control_selected']}
          FitControl_Selected: {blocks[blockID]['fit_control_selected']}
          NoiseChannelLevels: {blocks[blockID]['noise_channel_levels']}
          SpeechChannelLevels: {blocks[blockID]['speech_channel_levels']}
          TestListDefaultSubHeader: {blocks[blockID]['testlist_default_subheader']}
         }}
  """
  name = "mainSpeechProfile_TTABC"+str(nReps)+'reps_'+str(count)
  file_id = generate_random_id()
  fileName='Matrix_profiles\mainSpeechProfile_TTABC'+str(nReps)+'reps_'+str(count)+'.txt'
  generate_text_file(name, file_id, block_parameters, fileName)

# %%
