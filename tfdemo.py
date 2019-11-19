import tensorflow_hub as hub
import tensorflow as tf

word_to_embed = "dog"

elmo = hub.Module("https://tfhub.dev/google/elmo/2")
embedding_tensor = elmo([word_to_embed], as_dict=True)["word_emb"] # Use as_dict because I want the whole dict, then I select "word_emb"

with tf.Session() as sess:
  sess.run(tf.global_variables_initializer())
  embedding = sess.run(embedding_tensor)
  print(embedding.shape)
