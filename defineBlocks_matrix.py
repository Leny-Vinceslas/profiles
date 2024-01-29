#AUTHOR: LENY VINCESLAS 
#------> Pay attention "speech level" in the profile while "noise level" in the software 
def defineABCD():
    
  trains=dict([])
  blocks=dict([])
  #Define Rep structure and block parameters
  #Trainning1 ########################################
  trains[0]=dict(
      speechlevel='55',
      snr = 10,
      level_control = "OldenburgerLX 0.5",
      fit_control = "OldenburgerLX 0.5",
      level_control_selected = "OldenburgerLX 0.5",
      fit_control_selected = "OldenburgerLX 0.5",
      noise_channel_levels = "0 0",
      speech_channel_levels = "0 0",
      testlist_default_subheader = '10',
  )
  #Trainning2
  trains[1]=dict(
      speechlevel='70',
      snr = 5,
      level_control = "OldenburgerLX 0.5",
      fit_control = "OldenburgerLX 0.5",
      level_control_selected = "OldenburgerLX 0.5",
      fit_control_selected = "OldenburgerLX 0.5",
      noise_channel_levels = "0 0",
      speech_channel_levels = "0 0",
      testlist_default_subheader = '10',
  )

  #BlockA ###########################################
  blocks[0]=dict(
      speechlevel='70',
      snr = 5,
      level_control = "OldenburgerLX 0.8",
      fit_control = "OldenburgerLX 0.8",
      level_control_selected = "OldenburgerLX 0.8",
      fit_control_selected = "OldenburgerLX 0.8",
      noise_channel_levels = "0 0",
      speech_channel_levels = "0 0",
      testlist_default_subheader = '20',
  )

  #BlockB
  blocks[1]=dict(
      speechlevel='70',
      snr = 5,
      level_control = "OldenburgerLX 0.5",
      fit_control = "OldenburgerLX 0.5",
      level_control_selected = "OldenburgerLX 0.5",
      fit_control_selected = "OldenburgerLX 0.5",
      noise_channel_levels = "0 0",
      speech_channel_levels = "0 0",
      testlist_default_subheader = '20',
  )

  #BlockC
  blocks[2]=dict(
      speechlevel='70',
      snr = 5,
      level_control = "OldenburgerLX 0.2",
      fit_control = "OldenburgerLX 0.2",
      level_control_selected = "OldenburgerLX 0.2",
      fit_control_selected = "OldenburgerLX 0.2",
      noise_channel_levels = "0 0",
      speech_channel_levels = "0 0",
      testlist_default_subheader = '20',
  )

  #BlockD
  blocks[3]=dict(
      speechlevel='70',
      snr = 5,
      level_control = "OldenburgerWithSlope",
      fit_control = "OldenburgerWithSlope",
      level_control_selected = "OldenburgerWithSlope",
      fit_control_selected = "OldenburgerWithSlope",
      noise_channel_levels = "0 0",
      speech_channel_levels = "0 0",
      testlist_default_subheader = '30',
  )
  return trains, blocks

def defineABCSlope():
    
  trains=dict([])
  blocks=dict([])
  #Define Rep structure and block parameters
  #Trainning1 ########################################
  trains[0]=dict(
      speechlevel='55',
      snr = 10,
      level_control = "OldenburgerLX 0.5",
      fit_control = "OldenburgerLX 0.5",
      level_control_selected = "OldenburgerLX 0.5",
      fit_control_selected = "OldenburgerLX 0.5",
      noise_channel_levels = "0 0",
      speech_channel_levels = "0 0",
      testlist_default_subheader = '10',
  )
  #Trainning2
  trains[1]=dict(
      speechlevel='70',
      snr = 5,
      level_control = "OldenburgerLX 0.5",
      fit_control = "OldenburgerLX 0.5",
      level_control_selected = "OldenburgerLX 0.5",
      fit_control_selected = "OldenburgerLX 0.5",
      noise_channel_levels = "0 0",
      speech_channel_levels = "0 0",
      testlist_default_subheader = '10',
  )

  #BlockA ###########################################
  blocks[0]=dict(
      speechlevel='50',
      snr = 5,
      level_control = "OldenburgerWithSlope",
      fit_control = "OldenburgerWithSlope",
      level_control_selected = "OldenburgerWithSlope",
      fit_control_selected = "OldenburgerWithSlope",
      noise_channel_levels = "0 0",
      speech_channel_levels = "0 0",
      testlist_default_subheader = '30',
  )

  #BlockB
  blocks[1]=dict(
      speechlevel='60',
      snr = 5,
      level_control = "OldenburgerWithSlope",
      fit_control = "OldenburgerWithSlope",
      level_control_selected = "OldenburgerWithSlope",
      fit_control_selected = "OldenburgerWithSlope",
      noise_channel_levels = "0 0",
      speech_channel_levels = "0 0",
      testlist_default_subheader = '30',
  )

  #BlockC
  blocks[2]=dict(
      speechlevel='70',
      snr = 5,
      level_control = "OldenburgerWithSlope",
      fit_control = "OldenburgerWithSlope",
      level_control_selected = "OldenburgerWithSlope",
      fit_control_selected = "OldenburgerWithSlope",
      noise_channel_levels = "0 0",
      speech_channel_levels = "0 0",
      testlist_default_subheader = '30',
  )

  return trains, blocks