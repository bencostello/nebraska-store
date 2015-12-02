# -*- coding:utf-8 -*-
from ebaysdk.finding import Connection
from ebaysdk.shopping import Connection as Shopping
from ebaysdk.exception import ConnectionError
import time

def query_category(request, page, category_id):
    #parse query from filter
    query_attrs = {}

    #Condition
    conditions = ['1000', '1500', '1750']

    query_attrs['cond_new'] = request.GET.get('cond_new', '')
    if not query_attrs['cond_new']:
        conditions.remove('1000')

    query_attrs['cond_nwb'] = request.GET.get('cond_nwb', '')
    if not query_attrs['cond_nwb']:
        conditions.remove('1500')

    query_attrs['cond_def'] = request.GET.get('cond_def', '')
    if not query_attrs['cond_def']:
        conditions.remove('1750')

    if conditions == []:
     	conditions = ['1000']

    #Material
    materials = ['Leather', 'Suede', 'Patent Leather', 'Canvas', 'Rubber', 'Snakeskin', 'Synthetic', 'Vegan']

    query_attrs['leather'] = request.GET.get('leather', '')
    if not query_attrs['leather']:
        materials.remove('Leather')

    query_attrs['suede'] = request.GET.get('suede', '')
    if not query_attrs['suede']:
        materials.remove('Suede')

    query_attrs['patent_leather'] = request.GET.get('patent_leather', '')
    if not query_attrs['patent_leather']:
        materials.remove('Patent Leather')

    query_attrs['canvas'] = request.GET.get('canvas', '')
    if not query_attrs['canvas']:
        materials.remove('Canvas')

    query_attrs['rubber'] = request.GET.get('rubber', '')
    if not query_attrs['rubber']:
        materials.remove('Rubber')

    query_attrs['snakeskin'] = request.GET.get('snakeskin', '')
    if not query_attrs['snakeskin']:
        materials.remove('Snakeskin')

    query_attrs['synthetic'] = request.GET.get('synthetic', '')
    if not query_attrs['synthetic']:
        materials.remove('Synthetic')

    query_attrs['vegan'] = request.GET.get('vegan', '')
    if not query_attrs['vegan']:
        materials.remove('Vegan')

    # if materials == []:
    #  	materials = ['Leather']

    #Min and Max Prices
    query_attrs['min-price'] = request.GET.get('min-price', '')
    if not query_attrs['min-price']:
        query_attrs['min-price'] = '0'

    query_attrs['max-price'] = request.GET.get('max-price', '')
    if not query_attrs['max-price']:
        query_attrs['max-price'] = '1000'


    #US Shoes Sizes
    sizes = ['6', '6.5', '7', '7.5', '8', '8.5', '9', '9.5', '10']

    query_attrs['size6'] = request.GET.get('size6', '')
    if not query_attrs['size6']:
        del query_attrs['size6']
        sizes.remove('6')

    query_attrs['size6.5'] = request.GET.get('size6.5', '')
    if not query_attrs['size6.5']:
        del query_attrs['size6.5']
    	sizes.remove('6.5')

    query_attrs['size7'] = request.GET.get('size7', '')
    if not query_attrs['size7']:
        del query_attrs['size7']
    	sizes.remove('7')

    query_attrs['size7.5'] = request.GET.get('size7.5', '')
    if not query_attrs['size7.5']:
        del query_attrs['size7.5']
        sizes.remove('7.5')

    query_attrs['size8'] = request.GET.get('size8', '')
    if not query_attrs['size8']:
        del query_attrs['size8']
        sizes.remove('8')

    query_attrs['size8.5'] = request.GET.get('size8.5', '')
    if not query_attrs['size8.5']:
        del query_attrs['size8.5']
        sizes.remove('8.5')

    query_attrs['size9'] = request.GET.get('size9', '')
    if not query_attrs['size9']:
        del query_attrs['size9']
        sizes.remove('9')

    query_attrs['size9.5'] = request.GET.get('size9.5', '')
    if not query_attrs['size9.5']:
        del query_attrs['size9.5']
        sizes.remove('9.5')

    query_attrs['size10'] = request.GET.get('size10', '')
    if not query_attrs['size10']:
        del query_attrs['size10']
        sizes.remove('10')

    # if sizes == []:
    # 	sizes = ['7']

    #connect to ebay api and search items
    api = Connection(appid='*****')
    response = api.execute('findItemsIneBayStores', {
    'storeName': '*****', 
    'categoryId': category_id,

    'itemFilter': [
    {'name': 'ListingType','value': 'FixedPrice'},
    {'name': 'BIN','value': '1'},
    {'name':'MinPrice', 'value':query_attrs['min-price']},
    {'name':'MaxPrice', 'value':query_attrs['max-price']},
    {'name':'Condition', 'value':conditions},
    ], 

    'aspectFilter': [
    {'aspectName': 'Material', 'aspectValueName':materials},
    {'aspectName': 'US Shoe Size (Women\'s)', 'aspectValueName':sizes},
    ],

    'sortOrder':
    'PricePlusShippingLowest', 

    'paginationInput':
    {'entriesPerPage':'100', 'pageNumber':page}})

    time.sleep(1)
    
    try:
        items = response.reply.searchResult.item

        total_pages = response.reply.paginationOutput.totalPages
        total_entries = response.reply.paginationOutput.totalEntries

        imgs = []
        #price calculations
        for i in items:
            price = float(i.sellingStatus.currentPrice.value)
            price = price + price*0.15
            price = round(price, 2)
            if price < 10:
                price +=5

            elif 10 < price < 20:
                price +=2

            i.sellingStatus.currentPrice.value = str(price)
            i.title = i.title.rsplit(' ', 2)[0] #cutting Blemish blabla
            imgs.append([i.galleryPlusPictureURL, i.title, i.itemId, i.sellingStatus.currentPrice.value, i.condition.conditionDisplayName]) 
        return	{'imgs':imgs, 
        'category':category_id,
        'total_pages':total_pages, 
        'total_entries':total_entries,
        'minprice_selected':query_attrs['min-price'],
        'maxprice_selected':query_attrs['max-price'],}
    except:
    	return 0


def query_product(request, itemID):
    api = Shopping(appid='*****')
    response = api.execute('GetSingleItem', {'ItemID': itemID, 'IncludeSelector':'ShippingCosts, ItemSpecifics, Variations'})
    item = response.dict()
    
    #price calculations
    p = item['Item']['ConvertedCurrentPrice']['value']
    price = float(p)
    price = price + price*0.15
    price = round(price, 2)
    if price < 10:
        price +=10

    elif 10 < price < 20:
        price +=5

    #item specifics
    title = item['Item']['Title']
    title = title.rsplit(' ', 2)[0] #cutting Blemish blabla
    price = str(price)
    pics = item['Item']['PictureURL']
    condition = item['Item']['ConditionDisplayName']

    if condition == 'New with defects':
        condition_desc = item['Item']['ConditionDescription']
    else:
        condition_desc = '---'

    shipping = item['Item']['ShippingCostSummary']['ShippingServiceCost']['value']

    #retrieving item aspects by value
    dicts = item['Item']['ItemSpecifics']['NameValueList'] #if item has not variations
    var = item['Item'] # ready to retrieve variations
    size = []

    if var.has_key('Variations'):
    	var = var['Variations']['Variation']
    	for v in var:
    		size.append(v['VariationSpecifics']['NameValueList']['Value'])
    	size = ", ".join((str(s) for s in size))
    else:
    	try:
    		size = (it for it in dicts if it["Name"] == "US Shoe Size (Women's)").next()['Value']
    	except:
    		size = "no size"

    try:
    	width = (it for it in dicts if it["Name"] == "Width").next()['Value']
    except:
    	width = u"Не указано"
    material = (it for it in dicts if it["Name"] == "Material").next()['Value']
    color = (it for it in dicts if it["Name"] == "Color").next()['Value']
    kabluk = (it for it in dicts if it["Name"] == "Heel Height").next()['Value']

    return {'title':title, 
    'price':price, 
    'pics':pics, 
    'condition': condition, 
    'condition_desc':condition_desc,
    'shipping':shipping, 
    'size':size, 
    'width':width,
    'material':material, 
    'color':color, 
    'kabluk':kabluk}
