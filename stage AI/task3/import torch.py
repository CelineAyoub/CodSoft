# Load pre-trained image recognition model (e.g., ResNet)
image_model = tf.keras.applications.ResNet50(include_top=False, weights='imagenet')

# Extract image features
image_input = tf.keras.layers.Input(shape=(224, 224, 3))
image_features = image_model(image_input)
image_features = tf.keras.layers.Flatten()(image_features)
image_features = tf.keras.layers.Dense(256, activation='relu')(image_features)

# Load and preprocess caption data
# Define model architecture for caption generation (e.g., LSTM)
caption_input = tf.keras.layers.Input(shape=(max_caption_length,))
caption_embedding = tf.keras.layers.Embedding(vocab_size, embedding_dim)(caption_input)
caption_lstm = tf.keras.layers.LSTM(256)(caption_embedding)
caption_output = tf.keras.layers.Dense(vocab_size, activation='softmax')(caption_lstm)

# Combine image features and caption input
combined_input = tf.keras.layers.concatenate([image_features, caption_output])
decoder_lstm = tf.keras.layers.LSTM(512)(combined_input)
decoder_output = tf.keras.layers.Dense(vocab_size, activation='softmax')(decoder_lstm)

# Define the model
model = tf.keras.models.Model(inputs=[image_input, caption_input], outputs=decoder_output)

# Compile the model
model.compile(loss='categorical_crossentropy', optimizer='adam')

# Train the model
model.fit([image_data, caption_data], target_data, batch_size=32, epochs=10, validation_split=0.2)

# Generate captions for new images
def generate_caption(image):
    image_features = image_model.predict(image)
    initial_caption = np.zeros((1, max_caption_length))  # Initialize caption input
    caption = []
    for _ in range(max_caption_length):
        predictions = model.predict([image_features, initial_caption])
        predicted_word_index = np.argmax(predictions)
        caption.append(index_to_word[predicted_word_index])
        if index_to_word[predicted_word_index] == '<end>':
            break
        initial_caption[0][_] = predicted_word_index
    return ' '.join(caption)
