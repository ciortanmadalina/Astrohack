print('hello')
import tensorflow as tf
import csv

#convert to from ; separated to CSV
# outfile = open('hack/data/out.csv', 'a')
# with open("hack/data/sample.csv", buffering=200000, encoding='latin-1') as f:
#     csvreader = csv.reader(f, quotechar='"')
#     for line in csvreader:
#         line[-1] = line[-1].replace(';', ',')
#         print(line[-1])
#         outfile.write(line[-1])
#         outfile.write('\n')
#     outfile.close()

#filename_queue = tf.train.string_input_producer(["hack/data/Sample_Data/SAMPLE/1237645879578460255-g.csv"])
filename_queue = tf.train.string_input_producer(["hack/data/out.csv"])

reader = tf.TextLineReader(skip_header_lines=1)
_, csv_row = reader.read(filename_queue)
record_defaults = [[0.0],[0.0], [0.0], [0.0]]
col1, col2, col3, col4= tf.decode_csv(csv_row, record_defaults=record_defaults)
features = tf.stack([col1, col2, col3])

with tf.Session() as sess:
  # Start populating the filename queue.
  coord = tf.train.Coordinator()
  threads = tf.train.start_queue_runners(coord=coord)

  for i in range(1200):
    example, label = sess.run([features, col4])

  coord.request_stop()
  coord.join(threads)
