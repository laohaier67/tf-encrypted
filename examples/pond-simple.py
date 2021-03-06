import numpy as np
import tensorflow_encrypted as tfe
from tensorflow_encrypted.protocol import Pond

config = tfe.LocalConfig(3)

prot = Pond(*config.players)

# a = prot.define_constant(np.array([4, 3, 2, 1]).reshape(2,2))
# b = prot.define_constant(np.array([4, 3, 2, 1]).reshape(2,2))
# c = a * b

a = prot.define_private_variable(np.array([1., 2., 3., 4.]).reshape(2, 2))
b = prot.define_private_variable(np.array([1., 2., 3., 4.]).reshape(2, 2))
c = prot.define_private_variable(np.array([1., 2., 3., 4.]).reshape(2, 2))

x = (a * b)
y = (a * c)
z = x + y

w = prot.define_private_variable(np.zeros((2, 2)))

with config.session() as sess:
    # print(c.eval(sess, tag='c'))

    tfe.run(sess, prot.initializer, tag='init')
    tfe.run(sess, prot.assign(w, z), tag='assign')
    tfe.run(sess, prot.assign(w, z), tag='assign')

    print(w.reveal().eval(sess, tag='reveal'))

    # g.eval(sess, tag='g')

    # sess.run(prot.assign(d, f))
    # sess.run(prot.assign(e, e))

    # print(f.reveal().eval(sess))

    # g = prot.sigmoid(d)
    # print(g.reveal().eval(sess))

    # b = prot.define_private_placeholder(shape)

    # c = prot.define_private_variable()
    # d = prot.define_public_variable()
