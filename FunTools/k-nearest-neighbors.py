import math
import sys
from texttable import Texttable


#
#   use |A&B|/sqrt(|A || B |) to calculate cosine value
#
#
#
def calcCosDistSpe(user1,user2):
    avg_x=0.0
    avg_y=0.0
    for key in user1:
        avg_x+=key[1]
    avg_x=avg_x/len(user1)
    
    for key in user2:
        avg_y+=key[1]
    avg_y=avg_y/len(user2)
    
    u1_u2=0.0
    for key1 in user1:
        for key2 in user2:
            if key1[1] > avg_x and key2[1]>avg_y and key1[0]==key2[0]:
                u1_u2+=1
    u1u2=len(user1)*len(user2)*1.0
    sx_sy=u1_u2/math.sqrt(u1u2)
    return sx_sy


#
#   calculate cosine distance
#
#
def calcCosDist(user1,user2):
    sum_x=0.0
    sum_y=0.0
    sum_xy=0.0
    for key1 in user1:
        for key2 in user2:
            if key1[0]==key2[0] :
                sum_xy+=key1[1]*key2[1]
                sum_y+=key2[1]*key2[1]
                sum_x+=key1[1]*key1[1]
    
    if sum_xy == 0.0 :
        return 0
    sx_sy=math.sqrt(sum_x*sum_y) 
    return sum_xy/sx_sy


#
#
#   calculate cosine similarity
#
#
#
def calcSimlaryCosDist(user1,user2):
    sum_x=0.0
    sum_y=0.0
    sum_xy=0.0
    avg_x=0.0
    avg_y=0.0
    for key in user1:
        avg_x+=key[1]
    avg_x=avg_x/len(user1)
    
    for key in user2:
        avg_y+=key[1]
    avg_y=avg_y/len(user2)
    
    for key1 in user1:
        for key2 in user2:
            if key1[0]==key2[0] :
                sum_xy+=(key1[1]-avg_x)*(key2[1]-avg_y)
                sum_y+=(key2[1]-avg_y)*(key2[1]-avg_y)
        sum_x+=(key1[1]-avg_x)*(key1[1]-avg_x)
    
    if sum_xy == 0.0 :
        return 0
    sx_sy=math.sqrt(sum_x*sum_y) 
    return sum_xy/sx_sy
    

#
#   readfile
#
#
def readFile(file_name):
    contents_lines=[]
    f=open(file_name,"r")
    contents_lines=f.readlines()
    f.close()
    return contents_lines



#
#   unzip rating info，>user id\t diskid \t user rating\t time
#   input：dataset
#   output:unzipped rating info
#
def getRatingInformation(ratings):
    rates=[]
    for line in ratings:
        rate=line.split("\t")
        rates.append([int(rate[0]),int(rate[1]),int(rate[2])])
    return rates


#
#   generate user rating DS
#   
#   input: [[2,1,5],[2,4,2]...]
#   output:1.user score dict 2.movie dict
#   use dict，key is user id，value is movie raring，
#   rate_dic[2]=[(1,5),(4,2)].... represents user 2 rated movie 1 with score 5，rated movie 4 with score 2
#
def createUserRankDic(rates):
    user_rate_dic={}
    item_to_user={}
    for i in rates:
        user_rank=(i[1],i[2])
        if i[0] in user_rate_dic:
            user_rate_dic[i[0]].append(user_rank)
        else:
            user_rate_dic[i[0]]=[user_rank]
            
        if i[1] in item_to_user:
            item_to_user[i[1]].append(i[0])
        else:
            item_to_user[i[1]]=[i[0]]
            
    return user_rate_dic,item_to_user


#
#   find nearest neighbors
#   input: user ID，all user dict，all item dict
#   output: a list of nearest neighbors
#
def calcNearestNeighbor(userid,users_dic,item_dic):
    neighbors=[]
    #neighbors.append(userid)
    for item in users_dic[userid]:
        for neighbor in item_dic[item[0]]:
            if neighbor != userid and neighbor not in neighbors: 
                neighbors.append(neighbor)
      
    neighbors_dist=[]
    for neighbor in neighbors:
        dist=calcSimlaryCosDist(users_dic[userid],users_dic[neighbor])  #calcSimlaryCosDist  calcCosDist calcCosDistSpe
        neighbors_dist.append([dist,neighbor])
    neighbors_dist.sort(reverse=True)
    #print neighbors_dist
    return  neighbors_dist


#
#   use UserFC to recommend
#   input：file name,user ID, count of neighbors
#   output：recommended movie ID, input user movie list, reversed index，neighbor list
#
def recommendByUserFC(file_name,userid,k=5):
    
    #read file data
    test_contents=readFile(file_name)
    
    #conver file data to List[[user id, movie id, scores]...] 
    test_rates=getRatingInformation(test_contents)
    
    #format to dict data 
    #    1.user dict：dic[user id]=[(movie id,movie score)...]
    #    2.movie dict：dic[movie id]=[user id1, user id2...]
    test_dic,test_item_to_user=createUserRankDic(test_rates)
    
    #find neighbors
    neighbors=calcNearestNeighbor(userid,test_dic,test_item_to_user)[:k]
        
    recommend_dic={}
    for neighbor in neighbors:
        neighbor_user_id=neighbor[1]
        movies=test_dic[neighbor_user_id]
        for movie in movies:
            #print movie
            if movie[0] not in recommend_dic:
                recommend_dic[movie[0]]=neighbor[0]
            else:
                recommend_dic[movie[0]]+=neighbor[0]
    #print len(recommend_dic)
    
    #build recommendation list
    recommend_list=[]
    for key in recommend_dic:
        #print key
        recommend_list.append([recommend_dic[key],key])
    
    
    recommend_list.sort(reverse=True)
    #print recommend_list
    user_movies = [ i[0] for i in test_dic[userid]]

    return [i[1] for i in recommend_list],user_movies,test_item_to_user,neighbors
    
    

#
#
#   get movie list
#
#
#
def getMoviesList(file_name):
    #print sys.getdefaultencoding()
    movies_contents=readFile(file_name)
    movies_info={}
    for movie in movies_contents:
        movie_info=movie.split("|")
        movies_info[int(movie_info[0])]=movie_info[1:]
    return movies_info
    
    
    
#main
#input ： test user set
if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    movies=getMoviesList("/Users/wuyinghao/Downloads/ml-100k/u.item")
    recommend_list,user_movie,items_movie,neighbors=recommendByUserFC("/Users/wuyinghao/Downloads/ml-100k/u.data",179,80)
    neighbors_id=[ i[1] for i in neighbors]
    table = Texttable()
    table.set_deco(Texttable.HEADER)
    table.set_cols_dtype(['t',  # text 
                          't',  # float (decimal)
                          't']) # automatic
    table.set_cols_align(["l", "l", "l"])
    rows=[]
    rows.append([u"movie name",u"release", u"from userid"])
    for movie_id in recommend_list[:20]:
        from_user=[]
        for user_id in items_movie[movie_id]:
            if user_id in neighbors_id:
                from_user.append(user_id)
        rows.append([movies[movie_id][0],movies[movie_id][1],""])
    table.add_rows(rows)
    print table.draw()