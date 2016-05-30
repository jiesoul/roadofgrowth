# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib

zhfont = matplotlib.font_manager.FontProperties(fname="c:/windows/Fonts/yahei_mono.ttf")

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

#plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

#plt.title("名义DGP", fontproperties=zhfont)

#plt.ylabel("十亿美元", fontproperties=zhfont)
# plt.show()

movies = ["Annie hall", "Ben-Hur", "Caseblanca", "Gandhi", "West side Story"]
num_oscars = [5, 11, 3, 8, 10]

xs = [i + 0.1 for i, _ in enumerate(movies)]

plt.bar(xs, num_oscars)

plt.ylabel("所获奥斯卡金像奖数量", fontproperties=zhfont)
plt.title("我最喜爱的电影", fontproperties=zhfont)

plt.xticks([i + 0.5 for i, _ in enumerate(movies)], movies)

plt.show()
