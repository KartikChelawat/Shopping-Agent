import sqlite3
import os


DB_PATH=os.path.join(os.path.dirname(__file__),"store.db")


def get_product_rating(product_id:int)->dict:
    conn=sqlite3.connect(DB_PATH)
    cursor=conn.cursor()
    cursor.execute("SELECT AVG(rating) as avg_rating,COUNT(*) as review_count FROM reviews WHERE product_id=?",(product_id,))
    result=cursor.fetchone()
    conn.close()
    if result:
        return {"avg_rating": result[0], "review_count": result[1]}
    return {"avg_rating": None, "review_count": 0}

def get_ratings_for_product(product_ids:list[int])->list[dict]:
    if not product_ids:
        return []
    conn=sqlite3.connect(DB_PATH)
    cursor=conn.cursor()
    placeholders=','.join('?' for _ in product_ids)
    query=f"SELECT product_id, AVG(rating) as avg_rating, COUNT(*) as review_count FROM reviews WHERE product_id IN ({placeholders}) GROUP BY product_id"
    cursor.execute(query, product_ids)
    results=cursor.fetchall()
    conn.close()
    ratings_map={row[0]: {"avg_rating": round(row[1], 2), "review_count": row[2]} for row in results}
    return [{
        "product_id": pid,
        "avg_rating": ratings_map.get(pid,{}).get("avg_rating","0.0"),
        "review_count": ratings_map.get(pid, {}).get("review_count",0)
    }
    for pid in product_ids
    ]

if __name__=="__main__":

    print(get_product_rating(1))
    # print(get_ratings_for_product([1,2,3]))