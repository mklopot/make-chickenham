#!/usr/bin/python3

import jinja2

set_num = input("Set number: ")
share = input("share: ")
confirmation = input("confirmation: ")
batch = input("batch: ")
stickers = input("Sticker numbers (comma-separated): ").split(",")

with open("plate2-side1.jinja2") as f:
    t = jinja2.Template(f.read())
    rendered = t.render(share=share, confirmation=confirmation, batch=batch)
    with open("set"+set_num+"-plate2-side1.svg", 'w') as svgout:
        svgout.write(rendered)

with open("plate2-side2.jinja2") as f:
    t = jinja2.Template(f.read())
    rendered = t.render(stickers=stickers)
    with open("set"+set_num+"-plate2-side2.svg", 'w') as svgout:
        svgout.write(rendered)
