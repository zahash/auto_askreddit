from flask import Flask, jsonify, request
import tensorflow as tf
import gpt_2_simple as gpt2

app = Flask(__name__)

# http://localhost:5000/generate/?nsamples=4&temperature=0.7
sess = None
graph = None


@app.route("/generate/", methods=["GET"])
def index():
    global sess
    global graph

    temperature = float(request.args.get("temperature", 0.9))
    nsamples = int(request.args.get("nsamples", 1))
    batch_size = int(request.args.get("batch_size", 1))

    if not (0.0 <= temperature <= 1.0):
        temperature = 1.0

    #if not (0 < nsamples <= 10):
    #    nsamples = 10

    batch_size = min(batch_size, nsamples)

    with graph.as_default():
        text = gpt2.generate(
            sess,
            run_name="run2",
            length=250,
            temperature=temperature,
            nsamples=nsamples,
            batch_size=batch_size,
            prefix="<|startoftext|>",
            truncate="<|endoftext|>",
            include_prefix=False,
            return_as_list=True,
        )

    return jsonify({"titles": text})


def main():
    global sess
    global graph

    sess = gpt2.start_tf_sess()
    graph = tf.get_default_graph()

    gpt2.load_gpt2(sess, run_name="run2")

    app.run(port=5000, debug=True)


if __name__ == "__main__":
    main()
