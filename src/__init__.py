import os.path
import click


def formatted(colors, output_format):
    if output_format == 'txt':
        return '\n'.join(colors)
    elif output_format == 'html':
        color_table = []
        for color in colors:
            color_table.append('''
                <tr>
                  <td style="background-color: #{0}; width: 50px;">&nbsp;</td>
                  <td>#{0}</td>
                </tr>'''.format(color))

        return '''<html><body><table>{0}</table></body></html>'''.format(
            ''.join(color_table))
    else:
        return 'Error: invalid output format: {0}'.format(output_format)


@click.command()
@click.option('--language', '-l', show_default=True, default='pt', help='output language [available: pt, en, es].')
@click.option('--format', '-f', show_default=True, default='txt', help='output format [available: txt, html].')
@click.option('--no-numbers', '-n', flag_value=True, help='do not replace letter to numbers.')
@click.option('--word-list', '-w', help='word list file (one word by line).')
def l33tcolors(language, format, no_numbers, word_list):
    if not word_list:
        word_list = 'src/dicts/{0}.txt'.format(language)

    if not os.path.isfile(word_list):
        click.echo('Error: no such file: {0}'.format(word_list))
        return

    with open(word_list, 'r') as wordlist_file:
        words = [word.upper().strip() for word in wordlist_file.readlines() if len(word) == 7]

    letters = set('ABCDEFOIST')
    if no_numbers:
        letters -= set('OIST')

    plain_words = filter(lambda x: not set(x) - letters, words)
    if no_numbers:
        l33t_colors = plain_words
    else:
        l33t_colors = map(
            lambda x: x.replace('O', '0').replace('I', '1').replace('S', '5').replace('T', '7'),
            plain_words
        )

    click.echo(formatted(l33t_colors, format))
