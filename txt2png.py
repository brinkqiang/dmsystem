

# -*- coding: utf-8 -*-
import argparse
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams['font.family'] = ['SimHei']

def parse_args():
    parser = argparse.ArgumentParser(description='将文本文件转换为PNG图片')
    parser.add_argument('input_file', help='输入文本文件路径')
    parser.add_argument('output_file', help='输出PNG文件路径')
    parser.add_argument('--fontsize', type=int, default=14, help='字体大小 (默认: 14)')
    return parser.parse_args()

def create_png_from_text(input_file, output_file, fontsize=14):
    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()

        # Set up the figure and axes
        fig, ax = plt.subplots(figsize=(12, 36))

        # 添加文本到图形（临时）
        text_obj = ax.text(0.5, 0.5, text)

        # 绘制一次以获取文本边界框
        fig.canvas.draw()

        # 获取文本的边界框
        bbox = text_obj.get_window_extent()

        # 将像素坐标转换为图形坐标
        inv = ax.transData.inverted()
        bbox_data = bbox.transformed(inv)

        # 获取文本边界框的宽度和高度
        width = bbox_data.width
        height = bbox_data.height

        # 关闭初始图形
        plt.close(fig)

        # 创建新的图形，并设置大小以适应文本边界框
        fig, ax = plt.subplots(figsize=(width, height))

        # 隐藏坐标轴
        ax.axis('off')

        # 添加文本到新的图形
        ax.text(0.5, 0.5, text)

        # 保存图像
        plt.savefig(output_file, bbox_inches='tight', dpi=300)
        print("Saved to", output_file)


if __name__ == "__main__":
    args = parse_args()
    create_png_from_text(args.input_file, args.output_file, fontsize=args.fontsize)
