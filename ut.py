dataset = tf.data.Dataset.from_tensor_slices((x_train, y_train))
dataset = dataset.batch(32).prefetch(tf.data.AUTOTUNE)
