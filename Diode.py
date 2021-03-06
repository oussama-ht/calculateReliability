import re
class 二极管_可靠性_模型:
    __稳压_TVS_基本失效率 ={0: 0.060, 5: 0.062, 10: 0.065, 15: 0.067, 20: 0.070, 25: 0.073, 30: 0.077,
                          35: 0.080, 40: 0.084, 45: 0.089, 50: 0.094, 55: 0.100, 60: 0.107, 65: 0.115,
                          70: 0.125, 75: 0.137, 80: 0.152, 85: 0.170, 90: 0.194, 95: 0.224, 100: 0.0264}  # 基于 S = 0.5
    __稳压_TVS_环境系数 = {"GB": 1.0, "GMS": 1.2, "GF1": 1.7, "GF2": 5.0, "GM1": 5.5, "GM2": 11, "MP": 7.5, "NSB": 4.5,
                         "NS1": 3.0, "NS2": 6.0, "NU": 14, "AIF": 13, "AUF": 20, "AIC": 7.0, "AUC": 11, "ARW": 15,
                         "SF": 0.5, "ML": 28, "MF": 15}
    __稳压_TVS_质量系数 ={"A2": 0.03, "A3": 0.05, "A4": 0.1,
                        "A5": 0.2, "B1": 0.5, "B2": 1.0, "C": 5.0}
    __稳压_TVS_应用系数 = {"电压调整": 0.65,
                           "电压基准": 1.0,
                           "电流调整": 1.2}

    __普通锗二极管_基本失效率 = {0: 0.020, 5: 0.024, 10: 0.029, 15: 0.035, 20: 0.042, 25: 0.051, 30: 0.061,
                                35: 0.075, 40: 0.093, 45: 0.118, 50: 0.154, 55: 0.208, 60: 0.298}
    __普通硅二极管_基本失效率 = {0: 0.020, 5: 0.021, 10: 0.023, 15: 0.026, 20: 0.028, 25: 0.030, 30: 0.033,
                                35: 0.036, 40: 0.039, 45: 0.043, 50: 0.047, 55: 0.052, 60: 0.058, 65: 0.064,
                                70: 0.072, 75: 0.082, 80: 0.095, 85: 0.112, 90: 0.134, 95: 0.164, 100: 0.207}
    __普通二极管_环境系数 = {"GB": 1.0, "GMS": 1.2, "GF1": 1.7, "GF2": 5.0, "GM1": 5.5, "GM2": 11, "MP": 7.5, "NSB": 4.5,
                         "NS1": 3.0, "NS2": 6.0, "NU": 14, "AIF": 13, "AUF": 20, "AIC": 7.0, "AUC": 11, "ARW": 15,
                         "SF": 0.5, "ML": 28, "MF": 15}
    __普通二极管质量系数 = {"A2": 0.03, "A3": 0.05, "A4": 0.1,
                            "A5": 0.2, "B1": 0.4, "B2": 1.0, "C": 5.0}
    __普通二极管额定电流系数 = {"小于1A": 1.0, "1A到3A": 1.5,
                                "3A到10A": 2.0, "10A到20A": 3.0, "20A到50A": 4.0,"大于50A":5.0}
    __普通二极管应用系数 = {"小信号检波": 1.0, "逻辑开关": 0.6,
                            "电源整流": 1.5, "功率整流": 2.5}
    __普通二极管电压应力系数 = {0.3: 0.2, 0.4: 0.40, 0.5: 0.70, 0.6: 1.0, 0.7: 1.3, 0.8: 1.8,
                                0.9: 2.5, 1: 3.3}
    __普通二极管结构系数 = {"冶金键合": 1.0,
                            "弹性压力": 2.0}

    __工作温度 = 40
    __工作环境类别 = "GM1"
    __质量系数 = "B1"
    __稳压_TVS_应用场合 = "电压调整"
    __普通二极管应用场合 = "逻辑开关"
    __二极管类型 = "锗二极管"
    __普通二极管额定电流 = "小于1A"
    __普通二极管电压应力 = 0.5
    __普通二极管结构 = "冶金键合"

    def 得到_稳压_TVS_可靠性(self):
        step1 = self.__稳压_TVS_基本失效率[self.__工作温度]/1000000 * \
                self.__稳压_TVS_环境系数[self.__工作环境类别]
        step2 = self.__稳压_TVS_质量系数[self.__质量系数] * self.__稳压_TVS_应用系数[self.__稳压_TVS_应用场合]

        return step1 * step2
    def 得到普通二极管可靠性(self):
        if self.__二极管类型 == "锗二极管":
            step1 = self.__普通锗二极管_基本失效率[self.__工作温度] / 1000000 * \
                    self.__普通二极管_环境系数[self.__工作环境类别]
            step2 = self.__普通二极管质量系数[self.__质量系数] * self.__普通二极管额定电流系数[self.__普通二极管额定电流]

            step3 = self.__普通二极管应用系数[self.__普通二极管应用场合] *  \
                    self.__普通二极管电压应力系数[self.__普通二极管电压应力] * \
                    self.__普通二极管结构系数[self.__普通二极管结构]

            step4 = step1 * step2 * step3

            return  step4
        elif self.__二极管类型 == "硅二极管":
            step1 = self.__普通硅二极管_基本失效率[self.__工作温度] / 1000000 * \
                    self.__普通二极管_环境系数[self.__工作环境类别]
            step2 = self.__普通二极管质量系数[self.__质量系数] * self.__普通二极管额定电流系数[self.__普通二极管额定电流]

            step3 = self.__普通二极管应用系数[self.__普通二极管应用场合] * \
                    self.__普通二极管电压应力系数[self.__普通二极管电压应力] * \
                    self.__普通二极管结构系数[self.__普通二极管结构]

            step4 = step1 * step2 * step3

            return step4
        else:
            print("请确认普通二极管类型")
    def 得到可靠性(self):
        if re.search("TVS", self.__二极管类型):
            return self.得到_稳压_TVS_可靠性()
        elif re.search("稳压", self.__二极管类型):
            return self.得到_稳压_TVS_可靠性()
        else:
            return self.得到普通二极管可靠性()




    def __init__(self, 二极管类型, 工作温度, 工作环境类别, 质量系数, 稳压_TVS_应用场合 = "电压调整", 普通二极管应用场合= "逻辑开关",\
                 普通二极管额定电流 = "小于1A", 普通二极管电压应力 = 0.5, 普通二极管结构 = "冶金键合"):
        self.__二极管类型 = 二极管类型
        self.__工作温度 = 工作温度
        self.__工作环境类别 = 工作环境类别
        self.__质量系数 = 质量系数
        self.__稳压_TVS_应用场合 = 稳压_TVS_应用场合
        self.__普通二极管应用场合 = 普通二极管应用场合
        self.__普通二极管额定电流 = 普通二极管额定电流
        self.__普通二极管电压应力 = 普通二极管电压应力
        self.__普通二极管结构 = 普通二极管结构