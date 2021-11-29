import asyncio


async def input_main(data):
    import recaptcha

    car_mark = data['car_mark'].split(',')[0]
    part_number = data['car_mark'].split(',')[-1]
    # return recaptcha.find_past(part_number, car_mark)
    ret = await recaptcha.find_past(part_number, car_mark)
    return ret


# if __name__ == '__main__':
#     input_main({'car_mark': 'toyota, 52119-13340-A0'})