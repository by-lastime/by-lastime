from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets'
OUT.mkdir(exist_ok=True)
FONT = "-apple-system,BlinkMacSystemFont,'Segoe UI','PingFang SC','Microsoft YaHei',sans-serif"
INK = '#192744'
BLUE = '#3155EF'

def text(x, y, value, size=24, color=INK, weight=400):
    return f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" font-weight="{weight}" fill="{color}">{escape(value)}</text>'

def box(x, y, w, h, fill, radius=18, stroke='#CBD9F0'):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}"/>'

def line(x1, y1, x2, y2, color='#9FB2D6', width=2):
    return f'<path d="M{x1} {y1} L{x2} {y2}" fill="none" stroke="{color}" stroke-width="{width}" stroke-linecap="round"/>'

def arrow(x1, y, x2):
    return line(x1, y, x2, y, BLUE, 3) + f'<path d="M{x2-8} {y-7} L{x2} {y} L{x2-8} {y+7}" fill="none" stroke="{BLUE}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>'

def write(name, body, w=880, h=500, bg='#EAF2FF', label=''):
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{escape(label)}"><title>{escape(label)}</title>{box(1,1,w-2,h-2,bg,24)}{body}</svg>'
    (OUT / name).write_text(svg, encoding='utf-8')

def header():
    body = text(52, 61, 'BY-LASTIME / 十一', 17, '#53658B', 600)
    body += text(50, 124, '一点好奇，很多可能。', 44, INK, 700)
    body += text(52, 166, 'AI 应用 · 视觉计算 · 研究工具', 22, '#465D84')
    body += text(52, 215, '把想法做成能用的东西，也认真记录探索的过程。', 19, '#465D84')
    body += box(757, 39, 200, 174, '#FFFFF0', 22)
    body += box(780, 61, 150, 104, '#F1F5FF', 14)
    body += text(803, 127, '</>', 42, BLUE, 600)
    body += '<path d="M946 22 L951 37 L966 42 L951 47 L946 62 L941 47 L926 42 L941 37 Z" fill="none" stroke="#3155EF" stroke-width="2"/>'
    body += '<circle cx="770" cy="221" r="11" fill="#FFBE8F"/><circle cx="928" cy="230" r="8" fill="#A8BAFF"/>'
    write('header.svg', body, 1000, 264, '#E5EEFF', '十一 lastime：一点好奇，很多可能。AI 应用、视觉计算与研究工具。')

def paper_reader():
    body = text(42, 52, 'PAPER READER', 17, '#99745C', 600)
    body += text(42, 99, '在两种语言之间，读懂论文。', 32, INK, 700)
    body += box(42, 135, 366, 238, '#FFFDF9') + box(472, 135, 366, 238, '#FFFDF9')
    body += text(68, 175, 'EN / 原文', 23, '#806653', 600) + text(498, 175, '中文 / 对照', 23, '#806653', 600)
    for y in [215, 280]:
        body += box(62, y-21, 48, 29, '#FFE3CE', 8, '#FFE3CE') + text(70, y, 'B01' if y==215 else 'B02', 17, '#93664A', 600)
        body += box(492, y-21, 48, 29, '#FFE3CE', 8, '#FFE3CE') + text(500, y, 'B01' if y==215 else 'B02', 17, '#93664A', 600)
        for offset, width in [(0,237),(20,195),(40,215)]:
            body += line(125,y-7+offset,125+width,y-7+offset,'#C7BCB4',6)
            body += line(555,y-7+offset,555+width,y-7+offset,'#C7BCB4',6)
        arrow_body = arrow(421, y+3, 459)
        body += arrow_body
    body += text(47, 416, '稳定段落编号  /  公式与图表  /  原 PDF 页定位', 23, '#806653')
    body += text(47, 456, '问答批注可以长期保留', 23, '#806653')
    body += text(742, 475, '功能示意', 17, '#8D7564')
    write('paper-reader.svg', body, bg='#FFF0E4', label='论文双语阅读器功能示意：稳定段落编号与原文对照，来源定位，持久化批注。')

def research_workflow():
    body = text(42, 52, 'RESEARCH WORKFLOW', 17, '#857943', 600)
    body += text(42, 99, '把精读，变成一步步探索。', 32, INK, 700)
    for x, title, subtitle in [(42,'原文','核对来源'),(322,'讲义','解释与推导'),(602,'实验','数学与代码')]:
        body += box(x,149,236,109,'#FFFFF7') + text(x+30,191,title,28,INK,600) + text(x+30,230,subtitle,21,'#77764F')
    body += arrow(287,203,311) + arrow(567,203,591)
    body += box(322, 293, 236, 99, '#EDF4FF') + box(602, 293, 236, 99, '#EDF4FF')
    body += text(351,333,'独立作答',25,INK,600) + text(631,333,'证据与反馈',25,INK,600)
    body += text(351,368,'检查理解',20,'#5D7598') + text(631,368,'继续探索',20,'#5D7598')
    body += line(720,258,720,278,BLUE,3) + line(720,278,440,278,BLUE,3) + line(440,278,440,293,BLUE,3)
    body += arrow(567,340,591)
    body += text(47,449,'项目 skill · 材料工具 · 局部教学代码',23,'#77764F')
    body += text(742,475,'流程示意',17,'#8B825E')
    write('research-workflow.svg',body,bg='#FAFBE2',label='研究学习工作流示意：论文原文、讲义、实验、独立作答和反馈。')

def math_methods():
    body = text(42,52,'MATH METHOD BANK',17,'#7B70AA',600)
    body += text(42,99,'让知识和方法，连起来。',32,INK,700)
    body += box(42,152,218,109,'#FEFDFF') + text(68,194,'资料与来源',26,INK,600) + text(68,232,'页码 / 版本 / 核对',20,'#7B70AA')
    body += box(328,152,218,109,'#FEFDFF') + text(356,194,'题目与条件',26,INK,600) + text(356,232,'人工核对与审核',20,'#7B70AA')
    body += box(620,152,218,109,'#FEFDFF') + text(647,194,'知识与方法',26,INK,600) + text(647,232,'适用条件与边界',20,'#7B70AA')
    body += arrow(275,206,313) + arrow(559,206,605)
    body += box(328,302,510,88,'#EEF2FF') + text(356,353,'关联到具体解题步骤',27,INK,600)
    body += line(438,261,438,302,BLUE,3) + line(729,261,729,302,BLUE,3)
    body += text(47,448,'来源可追溯 · 方法可检查 · 结果经过审核',23,'#7B70AA')
    body += text(742,475,'结构示意',17,'#8A7BAA')
    write('math-methods.svg',body,bg='#F0EBFF',label='数学题库结构示意：来源、题目、知识与方法关联到具体解题步骤。')

header()
paper_reader()
research_workflow()
math_methods()
print('Generated header and 3 project previews.')
