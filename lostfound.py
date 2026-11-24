found=dict()
lost=[]
def add_item(typ,color,l,w,h,mat,place,name,phone):
    info={
        "color":color,
        "l":l,
        "w":w,
        "h":h,
        "mat":mat,
        "place":place,
        "name":name,
        "phone":phone
    }
    if typ not in found:
        found[typ]=[]
    found[typ].append(info)
def calc_score(want,item):
    score=0
    if want["color"]==item["color"]:
        score+=1
    if want["mat"]==item["mat"]:
        score+=1
    for k in["l","w","h"]:
        if want[k]*0.8<=item[k]<=want[k]*1.2:
            score+=1
    return score
while True:
    opt = input("\n请输入 find / lose / quit：")
    if opt == "quit":
        break
    elif opt == "find":
        typ = input("物品类型：")
        color = input("颜色：")
        l = float(input("长："))
        w = float(input("宽："))
        h = float(input("高："))
        mat = input("材质：")
        place = input("捡到地点：")
        name = input("捡到人名字：")
        phone = input("联系电话：")
        add_item(typ, color, l, w, h, mat, place, name, phone)
        print("✅ 录入成功！")
    elif opt == "lose":
        typ = input("丢失物品类型：")
        want = {}
        want["color"] = input("丢失物品颜色：")
        want["l"] = float(input("丢失物品长："))
        want["w"] = float(input("丢失物品宽："))
        want["h"] = float(input("丢失物品高："))
        want["mat"] = input("丢失物品材质：")
        result = []
        if typ in found:
            for item in found[typ]:
                score = calc_score(want, item)
                result.append( (score, item) )
        if result:
            print("\n---匹配结果---")
            for s, obj in result:
                print(f"分数：{s}，颜色：{obj['color']}，地点：{obj['place']}")
                best_score,best_item=result[0]
                confirm=input("是否确认？(y/n):")
                if confirm=="y":
                    found[typ].remove(best_item)
                    print（"认领成功"）
        else:
            print("❌ 暂时没有匹配到")
            lost.append(want)
