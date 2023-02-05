import os
import shutil

# Birinci klasörün yolunu belirti--->labels
folder1_path = "labels"

# İkinci klasörün yolunu belirtin--->images
folder2_path = "images"

# 3. klasörün yolunu belirtin-->to
folder3_path = "to_label"

# Birinci klasördeki dosyaları oku
for filename in os.listdir(folder1_path):
  # Dosyanın tam yolunu belirleyin
  file1_path = os.path.join(folder1_path, filename)

  # Dosya 2. klasörde yoksa dosyayı 3. klasöre kopyalayın
  if not os.path.exists(os.path.join(folder2_path, filename)):
    # Dosyanın 3. klasörde yoksa dosyayı kopyalayın
    if not os.path.exists(os.path.join(folder3_path, filename)):
      shutil.move(file1_path, folder3_path)
    else:
      # Dosya 3. klasörde varsa dosyayı yeniden adlandırın ve kopyalayın
      new_filename = "new_" + filename
      shutil.move(file1_path, os.path.join(folder3_path, new_filename))