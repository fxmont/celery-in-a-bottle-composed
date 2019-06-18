import random

import bottle

from tasks import divide


@bottle.route("/")
def index():
    top = random.randint(0, 100)
    bottom = random.randint(1, 100)

    result = divide.delay(top, bottom)

    answer = result.get(timeout=2.5)

    return {
        "equation": f"{top} / {bottom}",
        "answer": answer,
        "task_id": result.id,
    }


bottle.run(host="0.0.0.0", port=5000)
