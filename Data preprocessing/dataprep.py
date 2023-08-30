base_path = '.\\train_sample_videos\\'
dataset_path = '.\\prepared_dataset\\'
print('Creating Directory: ' + dataset_path)
os.makedirs(dataset_path, exist_ok=True)

tmp_fake_path = '.\\tmp_fake_faces'
print('Creating Directory: ' + tmp_fake_path)
os.makedirs(tmp_fake_path, exist_ok=True)

def get_filename_only(file_path):
    file_basename = os.path.basename(file_path)
    filename_only = file_basename.split('.')[0]
    return filename_only

with open(os.path.join(base_path, 'metadata.json')) as metadata_json:
    metadata = json.load(metadata_json)
    print(len(metadata))

real_path = os.path.join(dataset_path, 'real')
print('Creating Directory: ' + real_path)
os.makedirs(real_path, exist_ok=True)

fake_path = os.path.join(dataset_path, 'fake')
print('Creating Directory: ' + fake_path)
os.makedirs(fake_path, exist_ok=True)

############################################################################

for filename in metadata.keys():
    print(filename)
    print(metadata[filename]['label'])
    tmp_path = os.path.join(os.path.join(base_path, get_filename_only(filename)), 'faces')
    print(tmp_path)
    if os.path.exists(tmp_path):
        if metadata[filename]['label'] == 'real':    
            print('Copying to :' + real_path)
            copy_tree(tmp_path, real_path)
        elif metadata[filename]['label'] == 'fake':
            print('Copying to :' + tmp_fake_path)
            copy_tree(tmp_path, tmp_fake_path)
        else:
            print('Ignored..')