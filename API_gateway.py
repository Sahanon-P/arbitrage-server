from flask import Flask, jsonify, request
from Directed_graph import arbitrage
import time


app = Flask(__name__)

@app.route('/cycle', methods=['GET'])
def get_cycle():
    # price = 10
    price = request.args.get('price')
    price = float(price)
    print(type(price))
    start_time = time.time()
    list_token, last_price = arbitrage(price)
    end_time = time.time()

    total_profit = last_price - price
    percentage = (total_profit/price) * 100

    elapsed_time = end_time - start_time
    if list_token == None:
        return jsonify({
            'total_profit': 0,
            'percentage' : 0,
            'time_spending' : elapsed_time,
            'list_token' : []
        })
    
    return jsonify({
        'total_profit': total_profit,
        'percentage' : percentage,
        'time_spending' : elapsed_time,
        'list_token' : list_token
    })

if __name__ == '__main__':
    app.run(debug=True)