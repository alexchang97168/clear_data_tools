import pickle

f = open('C:/Users/Hjx/Desktop/商铺数据.csv','r',encoding='utf8')
for i in f.readlines()[:5]:
    print(i.split(','))
    
f.seek(0)
n = 0  # 创建计数变量
for i in f.readlines()[1:20]:
    data = i.split(',')
    #print(data)
    classify = data[0]             # 提取分类
    name = data[1]                 # 提取店铺名称
    comment_count = fcm(data[2])   # 提取评论数量
    star = data[3]                 # 提取星级
    price = fpr(data[4])           # 提取人均
    add = data[5]                  # 提取地址
    qua = fcl(data[6])[0]          # 提取质量评分
    env = fcl(data[6])[1]          # 提取环境评分
    ser = fcl(data[6])[2]          # 提取服务评分
    if  '缺失数据' not in [comment_count, price, qua]:   # 用于判断是否有数据缺失
        n += 1
        data_re = [['classify',classify],
                  ['name',name],
                  ['comment_count',comment_count],
                  ['star',star],
                  ['price',price],
                  ['address',add],
                  ['quality',qua],
                  ['environment',env],
                  ['service',ser]]
        datalst.append(dict(data_re))   # 生成字典，并存入列表datalst
        print('成功加载%i条数据' %n)
    else:
        continue
    
print(datalst) 
print('总共加载%i条数据' %n)

pic = open('C:/Users/Hjx/Desktop/data.pkl','wb')
pickle.dump(datalst,pic)
pic.close()
print('finished!')
# 将数据存成了pkl文件
