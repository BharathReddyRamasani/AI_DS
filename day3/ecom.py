def discount(tp, dper):
    dis = tp * dper / 100
    tp_after_discount = tp - dis
    return tp_after_discount, dis
def gst(tp, gper=18):
    gp = tp * gper / 100
    tp_after_gst = tp + gp
    return tp_after_gst, gp

def gen(cart, dper, gper=18):
    tp = sum(cart.values())
    print("Cart items:", cart)
    print(f"Subtotal: {tp}")
    tp_after_discount, dis = discount(tp, dper)
    print(f"Discount ({dper}%): -{dis}")
    print(f"Total after discount: {tp_after_discount}")
    tp_after_gst, gst_amount = gst(tp_after_discount, gper)
    print(f"GST ({gper}%): +{gst_amount}")
    print(f"Final Total: {tp_after_gst}")
