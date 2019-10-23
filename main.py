import PIL.ImageFont
import PIL.ImageDraw
import PIL.Image
import discord.ext.commands
import logging
import io

logging.basicConfig(level=logging.INFO)

text = "allie"

font = PIL.ImageFont.truetype("font.ttf", 200)
font_s = PIL.ImageFont.truetype("font2.ttf", 50)
blue = (26,52,84)
red = (218,64,50)

def draw_text(text):
  img = PIL.Image.open("blank.png")
  draw = PIL.ImageDraw.Draw(img)

  posx = 240
  posy = 200

  size = draw.textsize("Get ", font=font)
  draw.text((posx, posy),"Get", blue, font=font)
  posx += size[0]

  size = draw.textsize("ready", font=font)
  draw.text((posx, posy),"ready", red, font=font)
  posx += size[0]

  draw.text((posx, posy)," for", blue, font=font)
  posy += size[1]

  posx = 240
  draw.text((posx, posy), text.title(), blue, font=font)

  posx = 430
  posy = 835

  size = draw.textsize(f"Get ready for {text.title()} at ", font=font_s)
  draw.text((posx, posy),f"Get ready for {text.title()} at ", blue, font=font_s)
  posx += size[0]

  size = draw.textsize(f"gov.uk/{text.lower().replace(' ', '-')}", font=font_s)
  draw.text((posx, posy), f"gov.uk/{text.lower().replace(' ', '-')}", red, font=font_s)

  draw.line((posx, posy + size[1] + 10, posx + size[0], posy + size[1] + 10), fill=red, width=7)

  return img

bot = discord.ext.commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def brexit(ctx, *, text):
    img = draw_text(text)
    img_b = io.BytesIO()
    img.save(img_b, format='PNG')
    img_b.seek(0)
    await ctx.send(file=discord.File(img_b, filename="brexit.png"))

bot.run('NjM2Mjg5NTQ2OTIwOTE5MDQ1.Xa9c5g.M7KB_sRuwoO2o-9Njaulrn8mVIg')
