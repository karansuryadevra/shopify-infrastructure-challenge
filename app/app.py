from flask import Flask, render_template, request,redirect, send_file
from models import db, InventoryModel
import csv
import pandas as pd

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()

# Create
@app.route('/data/create', methods = ['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('createpage.html')
    
    if request.method == 'POST':
        inventory_id = request.form['inventory_id']
        name = request.form['name']
        description = request.form['description']
        count = request.form['count']

        inventory = InventoryModel(inventory_id=inventory_id, name=name, description=description, count=count)
        db.session.add(inventory)
        db.session.commit()
        return redirect('/data')

@app.route('/')
def home():
    return redirect('/data')

# Read
@app.route('/data')
def read():
    inventoryList = InventoryModel.query.all()
    return render_template('list.html', inventory_list=inventoryList)

@app.route('/data/<int:id>')
def readSingleInventory(id):
    inventorySingle = InventoryModel.query.filter_by(inventory_id=id).first()
    if inventorySingle:
        return render_template('singleInventory.html', inventory=inventorySingle) # done differently to tutorial
    return f"Inventory with {id} does not exist"

# Update
@app.route('/data/<int:id>/update', methods=['GET', 'POST'])
def update(id):
    inventory = InventoryModel.query.filter_by(inventory_id=id).first()
    print('inventory = ' + str(inventory))
    if request.method == 'POST':
        if inventory:
            inventory.inventory_id = request.form['inventory_id']
            inventory.name = request.form['name']
            inventory.description = request.form['description']
            inventory.count = request.form['count']
            db.session.commit()
            return redirect(f'/data/{inventory.inventory_id}')
        return f"Inventory with id:{id} does not exist"
    return render_template('update.html', inventory=inventory)

# Delete
@app.route('/data/<int:id>/delete', methods=['GET', 'POST'])
def delete(id):
    inventory = InventoryModel.query.filter_by(inventory_id=id).first()
    print('Request method is ' + request.method)
    if request.method == 'POST':
        if inventory:
            db.session.delete(inventory)
            db.session.commit()
            return redirect('/data')
        abort(404)
    return render_template('delete.html')

# Export
@app.route('/data/export')
def export():

    tupleValues = []
    # Return names of the columns to use as Headers for the CSV
    keys = InventoryModel.__table__.columns.keys()
    values = InventoryModel.query.all()
    keys = keys[1:]

    newValues = db.session.query(InventoryModel).all()
    print('newValues ', str(newValues))
    print('keys ', keys)

    for value in newValues:
        print(value.inventory_id, value.name, value.description, value.count)
        tupleValues.append((value.inventory_id, value.name, value.description, value.count))

    
    print('tupleValues is ', tupleValues)

    if request.method == 'GET':
        if keys:
            df = pd.DataFrame(tupleValues, columns=[keys])
            print(df)
            df.to_csv('./export.csv', index=False)
    
    return render_template('export.html')

@app.route('/data/return-file')
def download():
    return send_file('export.csv', as_attachment=True)



            
            


app.run(host='localhost', port=5000)