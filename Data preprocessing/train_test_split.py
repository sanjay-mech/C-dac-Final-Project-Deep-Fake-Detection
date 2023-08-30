random_faces = np.random.choice(all_fake_faces, len(all_real_faces), replace=True)
for fname in random_faces:
    src = os.path.join(tmp_fake_path, fname)
    dst = os.path.join(fake_path, fname)
    shutil.copyfile(src, dst)

print('Down-sampling Done!')

# Split into Train/ Val/ Test folders
splitfolders.ratio(dataset_path, output='split_dataset', seed=1377, ratio=(.8, .1, .1)) # default values
print('Train/ Val/ Test Split Done!')



input_size = 128
batch_size_num = 32
train_path = os.path.join('.\\split_dataset\\', 'train')
val_path = os.path.join('.\\split_dataset\\', 'val')
test_path = os.path.join('.\\split_dataset\\', 'test')
