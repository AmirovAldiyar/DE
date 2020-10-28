from View import NamedLineEdit

class SolutionPageData:
    def __init__(self, step, x_0, X, y_0):
        self._lineedits = [[],[],[],[]]
        self._lte = [[],[],[]]
        self._gte = [0,0,0]
        self.set_params(step, x_0, X, y_0)
        self.recalculate()



    def f(self, x, y):
        return -(float(y)**2)/3-2/(3*(x**2))

    def recalculate_em(self, step, x_0, X, y_0):
        result = [[float(x_0), ], [float(y_0), ], [255, 0, 0]]
        lte=[[float(x_0), ],[0,],[255,0,0]]
        gte=0
        h = (float(X) - float(x_0)) / float(step)
        for i in range(0, int(step)+1):
            y = float(result[1][i])
            x = float(result[0][i])
            result[0].append(float(x) + float(h))
            result[1].append(float(y) + float(h) * self.f(float(x), float(y)))

            # lte[1].append(self._lineedits[1][1][i + 1] - float(self._lineedits[1][1][i]) - float(h) * self.f(float(x), float(self._lineedits[1][1][i])))
            lte[1].append(result[1][i+1] - self._lineedits[1][1][i + 1])
            lte[0].append(x + float(h))

            gte = gte if gte > abs(result[1][i+1] - self._lineedits[1][1][i + 1]) else abs(result[1][i+1] - self._lineedits[1][1][i + 1])

        self._lineedits[0] = result
        self._gte[0] = gte
        self._lte[0] = lte

    def recalculate_ex(self, step, x_0, X, y_0):
        result = [[float(x_0), ], [float(y_0), ], [255, 255, 255]]
        h = (float(X) - float(x_0)) / float(step)
        for i in range(0, int(step)+1):
            y = float(result[1][i])
            x = float(result[0][i])
            result[0].append(float(x) + float(h))
            result[1].append(2.0/float(result[0][i+1]))

        self._lineedits[1] = result

    def recalculate_iem(self, step, x_0, X, y_0):
        result = [[float(x_0), ], [float(y_0), ], [0, 255, 0]]
        lte=[[float(x_0), ],[0,],[0,255,0]]
        gte=0
        h = (float(X) - float(x_0)) / float(step)

        for i in range(0, int(step)+1):
            y = float(result[1][i])
            x = float(result[0][i])
            h = float(h)

            result[0].append(x + h)
            result[1].append(y + h*(self.f(x,y) + self.f(x+h,y+h*self.f(x,y)))/2)

            # lte[1].append(self._lineedits[1][1][i + 1] - (self._lineedits[1][1][i] + h*(self.f(x,self._lineedits[1][1][i]) + self.f(x+h,self._lineedits[1][1][i]+h*self.f(x,self._lineedits[1][1][i])))/2))
            lte[1].append(result[1][i+1] - self._lineedits[1][1][i + 1])
            lte[0].append(x + h)

            gte = gte if gte > abs(result[1][i+1] - self._lineedits[1][1][i + 1]) else abs(result[1][i+1] - self._lineedits[1][1][i + 1])

        self._gte[1]=gte
        self._lineedits[2] = result
        self._lte[1] = lte

    def recalculate_rkm(self, step, x_0, X, y_0):

        def inc(x,y,h):
            k1 = h * float(self.f(x,y))
            k2 = h *float(self.f(x + h/2.0,y+k1/2.0))
            k3 = h * float(self.f(x + h/2.0,y+k2/2.0))
            k4 = h * float(self.f(x + h, y + k3))
            return [x + h, y + (1/6.0)*(k1 + 2.0 * k2 + 2.0 * k3 + k4)]

        result = [[float(x_0), ], [float(y_0), ], [0, 0, 255]]
        h = (float(X) - float(x_0)) / float(step)
        lte=[[float(x_0), ],[0,],[0,0,255]]
        gte=0

        for i in range(0, int(step)+1):
            y = float(result[1][i])
            x = float(result[0][i])
            h = float(h)
            k1 = h * float(self.f(x,y))
            k2 = h *float(self.f(x + h/2.0,y+k1/2.0))
            k3 = h * float(self.f(x + h/2.0,y+k2/2.0))
            k4 = h * float(self.f(x + h, y + k3))
            res = inc(x , y, h)
            result[0].append(res[0])
            result[1].append(res[1])
            lte[1].append(result[1][i+1] - self._lineedits[1][1][i + 1])
            # lte[1].append(self._lineedits[1][1][i + 1] - inc(x, self._lineedits[1][1][i], h)[1])
            lte[0].append(res[0])
            gte = gte if gte > abs(result[1][i+1] - self._lineedits[1][1][i + 1]) else abs(result[1][i+1] - self._lineedits[1][1][i + 1])

        self._lineedits[3] = result
        self._gte[2] = gte
        self._lte[2] = lte

    def recalculate(self):
        self.recalculate_ex(self.step, self.x_0, self.X, self.y_0)
        self.recalculate_em(self.step, self.x_0, self.X, self.y_0)
        self.recalculate_iem(self.step, self.x_0, self.X, self.y_0)
        self.recalculate_rkm(self.step, self.x_0, self.X, self.y_0)

    def set_params(self, step, x_0, X, y_0):
        self.step =step
        self.X =X
        self.x_0 =x_0
        self.y_0 =y_0

    def get_lineedits(self):
        return self._lineedits

    def get_lte(self):
        return self._lte

    def get_gte(self, n_0, N):
        res_em = [[],[],[255,0,0]]
        res_iem = [[],[],[0,255,0]]
        res_rkm = [[],[],[0,0,255]]
        for i in range(n_0, N+1):
            self.set_params(i, self.x_0, self.X, self.y_0)
            self.recalculate()
            res_em[0].append(i)
            res_em[1].append(self._gte[0])
            res_iem[0].append(i)
            res_iem[1].append(self._gte[1])
            res_rkm[0].append(i)
            res_rkm[1].append(self._gte[2])
        print(res_iem)
        return [res_em, res_iem, res_rkm]

