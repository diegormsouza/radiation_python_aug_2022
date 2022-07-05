#-----------------------------------------------------------------------------------------------------------
# INPE / CGCT / DISSM - Training: Radiation Data Processing With Python - Data Access with Python (CPTEC FTP)
# Author: Diego Souza (INPE / CGCT / DISSM)
#-----------------------------------------------------------------------------------------------------------

# Required modules
from datetime import datetime, timedelta # Basic Dates and time types
import os                                # Miscellaneous operating system interfaces
import time as t                         # Time access and conversion                                          
from ftplib import FTP                   # FTP protocol client

#-----------------------------------------------------------------------------------------------------------

def download_RAD(product, date, path_dest):

  # FTP data description:

  # GLOBAL SOLAR RADIATION:
  # Instantaneous   : http://ftp.cptec.inpe.br/goes/goes16/rad_solar/irradiancia_glb_bin/
  # Daily Average   : http://ftp.cptec.inpe.br/goes/goes16/rad_solar/irradiancia_glb_media_diaria_bin/
  # Monthly Average : http://ftp.cptec.inpe.br/goes/goes16/rad_solar/irradiancia_glb_media_mensal_bin/
  # 'GSR_I', 'GSR_D', 'GSR_M'

  # SOLAR UV + VISIBLE RADIATION:
  # Instantaneous   : http://ftp.cptec.inpe.br/goes/goes16/rad_solar/irradiancia_uv_vis_bin/
  # Daily Average   : http://ftp.cptec.inpe.br/goes/goes16/rad_solar/irradiancia_uv_vis_media_diaria_bin/
  # Monthly Average : http://ftp.cptec.inpe.br/goes/goes16/rad_solar/irradiancia_uv_vis_media_mensal_bin/
  # 'UVR_I', 'UVR_D', 'UVR_M'

  # INSOLATION:
  # Daily           : http://ftp.cptec.inpe.br/goes/goes16/rad_solar/insol_diaria_bin/
  # Biweekly        : http://ftp.cptec.inpe.br/goes/goes16/rad_solar/insol_quinzenal_bin/
  # Monthly         : http://ftp.cptec.inpe.br/goes/goes16/rad_solar/insol_mensal_bin/
  # 'INS_D', 'INS_B', 'INS_M'

  # OUTGOING LONGWAVE RADIATION:
  # 3 Hours         : http://ftp.cptec.inpe.br/goes/goes16/rad_solar/rol_3h_bin/
  # Daily Average   : http://ftp.cptec.inpe.br/goes/goes16/rad_solar/rol_media_diaria_bin/
  # 'OLR_3', 'OLR_D'

  # ULTRAVIOLET RADIATION:
  # Attenuated Ultraviolet Index : http://ftp.cptec.inpe.br/ncep/radiacao_uv/iuv_inst_atenuado_bin/
  # 'IUV'
  # Maximum UVI (Without Clouds) : http://ftp.cptec.inpe.br/ncep/radiacao_uv/iuv_max_snuvens_bin/
  # 'MUV'
  # Daily Ozone Content          : http://ftp.cptec.inpe.br/ncep/radiacao_uv/conteudo_oz_bin/
  # 'OZO'

  # DEVIATION
  # Monthly Deviation - Solar UV + Visible Radiation : http://ftp.cptec.inpe.br/goes/goes16/rad_solar/desvio_media_mensal_irra_uv_vis_bin/
  # DEV_U
  # Monthly Deviation - Radiation                    : http://ftp.cptec.inpe.br/goes/goes16/rad_solar/desvio_media_mensal_irradiancia_bin/
  # DEV_I

  print('------------------------------------')
  print('CPTEC FTP Download - Script started.')
  print('------------------------------------')

  # Start the time counter
  start_time = t.time()  

  #-----------------------------------------------------------------------------------------------------------

  # Download directory
  dir = "Samples"; os.makedirs(dir, exist_ok=True)

  # Product selection 
  product = product
  # Options: 
  # 'GSR_D' - GLOBAL SOLAR RADIATION: Instantaneous
  # 'GSR_I' - GLOBAL SOLAR RADIATION: Daily Average 
  # 'GSR_M' - GLOBAL SOLAR RADIATION: Monthly Average
  # 'UVR_I' - SOLAR UV + VISIBLE RADIATION: Instantaneous
  # 'UVR_D' - SOLAR UV + VISIBLE RADIATION: Daily Average 
  # 'UVR_M' - SOLAR UV + VISIBLE RADIATION: Monthly Average
  # 'INS_D' - INSOLATION: Daily
  # 'INS_B' - INSOLATION: Biweekly
  # 'INS_M' - INSOLATION: Monthly
  # 'OLR_3' - OUTGOING LONGWAVE RADIATION: 3 Hours
  # 'OLR_D' - OUTGOING LONGWAVE RADIATION: Daily Average
  # 'UVR_A' - ULTRAVIOLET RADIATION: Attenuated Ultraviolet Index
  # 'UVR_M' - ULTRAVIOLET RADIATION: Maximum UVI (Without Clouds)
  # 'OZO_D' - OZONE: Daily Ozone Content
  # 'DEV_U' - Monthly Deviation - Solar UV + Visible Radiation
  # 'DEV_I' - Monthly Deviation - Radiation 

  # Desired year (four digit)
  year = date[0:4]
  #year = '2022' 

  # Desired month (two digit)
  month = date[4:6]
  #month = '01'

  # Desired day (two digit)
  day = date[6:8] 
  #day = '01' 

  # Desired hour (two digit)
  hour = date[8:10] 
  #hour = '12'

  # Desired minutes (two digit)
  minute = date[10:12]
  #minute = '00'

  #-----------------------------------------------------------------------------------------------------------

  # FTP Address
  ftp = FTP('ftp.cptec.inpe.br') 

  # FTP Credentials 
  ftp.login('', '') 

  #-----------------------------------------------------------------------------------------------------------

  # Access the FTP folder, based on the desired product

  # GLOBAL SOLAR RADIATION:

  # Daily Average
  if (product == 'GSR_D'):
      # FTP Path
      path = ('goes/goes16/rad_solar/irradiancia_glb_media_diaria_bin/' + year + '/' + month + '/')
      naming_convention = 'S11636061'
      extension = '.bin'
      file_name = naming_convention + '_' + year + month + day + '0000' + extension

  # Instantaneous
  if (product == 'GSR_I'):
      # FTP Path
      path = ('goes/goes16/rad_solar/irradiancia_glb_bin/' + year + '/' + month + '/')
      naming_convention = 'S11636057'
      extension = '.bin'
      file_name = naming_convention + '_' + year + month + day + hour + minute + extension

  # Monthly Average
  if (product == 'GSR_M'):
      # FTP Path
      path = ('goes/goes16/rad_solar/irradiancia_glb_media_mensal_bin/' + year + '/' + month + '/')
      naming_convention = 'S11636064'
      extension = '.bin'
      file_name = naming_convention + '_' + year + month + '01' + '00' + '00' + extension

  # SOLAR UV + VISIBLE RADIATION:

  # Instantaneous
  elif (product == 'UVR_I'):
      # FTP Path
      path = ('goes/goes16/rad_solar/irradiancia_uv_vis_bin/' + year + '/' + month + '/')
      naming_convention = 'S11636058'
      extension = '.vis'
      file_name = naming_convention + '_' + year + month + day + hour + minute + extension

  # Daily Average
  elif (product == 'UVR_D'):
      # FTP Path
      path = ('goes/goes16/rad_solar/irradiancia_uv_vis_media_diaria_bin/' + year + '/' + month + '/')
      naming_convention = 'S11636062'
      extension = '.vis'
      file_name = naming_convention + '_' + year + month + day + hour + '00' + extension

  # Monthly Average
  elif (product == 'UVR_M'):
      # FTP Path
      path = ('goes/goes16/rad_solar/irradiancia_uv_vis_media_mensal_bin/' + year + '/' + month + '/')
      naming_convention = 'S11636065'
      extension = '.vis'
      file_name = naming_convention + '_' + year + month + '01' + '00' + '00' + extension

  # INSOLATION:

  # Daily
  elif (product == 'INS_D'):
      # FTP Path
      path = ('goes/goes16/rad_solar/insol_diaria_bin/' + year + '/' + month + '/')
      naming_convention = 'S11636081'
      extension = '.bin'
      file_name = naming_convention + '_' + year + month + day + '0000' + extension

  # Biweekly
  elif (product == 'INS_B'):
      # FTP Path
      path = ('goes/goes16/rad_solar/insol_quinzenal_bin/' + year + '/' + month + '/')
      naming_convention = 'S11636083'
      extension = '.bin'
      file_name = naming_convention + '_' + year + month + day + '0000' + extension

  # Monthly
  elif (product == 'INS_M'):
      # FTP Path
      path = ('goes/goes16/rad_solar/insol_mensal_bin/' + year + '/' + month + '/')
      naming_convention = 'S11636085'
      extension = '.bin'
      file_name = naming_convention + '_' + year + month + '01' + '00' + '00' + extension

  # OUTGOING LONGWAVE RADIATION:

  # 3 Hours
  elif (product == 'OLR_3'):
      # FTP Path
      path = ('goes/goes16/rad_solar/rol_3h_bin/' + year + '/' + month + '/')
      naming_convention = 'S11636069'
      extension = '.bin'
      file_name = naming_convention + '_' + year + month + day + hour + '00' + extension

  # Daily Average
  elif (product == 'OLR_D'):
      # FTP Path
      path = ('goes/goes16/rad_solar/rol_media_diaria_bin/' + year + '/' + month + '/')
      naming_convention = 'S11636071'
      extension = '.bin'
      file_name = naming_convention + '_' + year + month + day + '0000' + extension

  # ULTRAVIOLET RADIATION:

  # Attenuated Ultraviolet Index
  elif (product == 'UVR_A'):
      # FTP Path
      path = ('ncep/radiacao_uv/iuv_inst_atenuado_bin/' + year + '/' + month + '/')
      naming_convention = 'M16724009'
      extension = '.bin'
      file_name = naming_convention + '_' + year + month + day + hour + '00' + extension

  # Maximum UVI (Without Clouds)
  elif (product == 'UVR_M'):
      # FTP Path
      path = ('ncep/radiacao_uv/iuv_max_snuvens_bin/' + year + '/' + month + '/')
      naming_convention = 'M16724003'
      extension = '.bin'
      file_name = naming_convention + '_' + year + month + day + '0000' + extension

  # Daily Ozone Content
  elif (product == 'OZO_D'):
      # FTP Path
      path = ('ncep/radiacao_uv/conteudo_oz_bin/' + year + '/' + month + '/')
      naming_convention = 'M16724006'
      extension = '.bin'
      file_name = naming_convention + '_' + year + month + day + '0000' + extension

  # DEVIATION

  # Monthly Deviation - Solar UV + Visible Radiation
  elif (product == 'DEV_U'):
      # FTP Path
      path = ('/goes/goes16/rad_solar/desvio_media_mensal_irra_uv_vis_bin/' + year + '/' + month + '/')
      naming_convention = 'S11636068'
      extension = '.vis'
      file_name = naming_convention + '_' + year + month + '01' + '00' + '00' + extension

  # Monthly Deviation - Radiation
  elif (product == 'DEV_I'):
      # FTP Path
      path = ('/goes/goes16/rad_solar/desvio_media_mensal_irradiancia_bin/' + year + '/' + month + '/')
      naming_convention = 'S11636067'
      extension = '.bin'
      file_name = naming_convention + '_' + year + month + '01' + '00' + '00' + extension

  #-----------------------------------------------------------------------------------------------------------

  # Download the file
  print('\n---------------------')
  print('Checking the FTP File:') 
  print('---------------------')
  print('Product: ' + product)
  print('Date: ' + year + month + day)
  print('File Name: ' + file_name)

  try:
    # Enter the FTP Path
    ftp.cwd(path)
    # Check if the file exists
    if os.path.exists(dir + '//' + file_name):
      print("")
      print('The file ' + dir + '/' + file_name + ' already exists.')
      print("")
    else:
      # If not, download the file
      ftp.retrbinary("RETR " + file_name, open(dir + '//' + file_name, 'wb').write)  
      print("Downloading the file...")
      print("")
      print('\n---------------------')
      print('Download Finished.') 
      print('---------------------')
      print("")
      # End the time counter
      print('\nTotal Download Time:', round((t.time() - start_time),2), 'seconds.') 
      print("")
  except:
    print("\nFile not available!")

  # Quit the FPT connection
  ftp.quit()

  #-----------------------------------------------------------------------------------------------------------
  # Return the file name
  return f'{file_name}'
  #-----------------------------------------------------------------------------------------------------------