"""
Task 1: CSV Statistics
读取 CSV 文件，打印每列的统计信息：行数、非空数、唯一值数
"""
import csv
import sys
from pathlib import Path


def analyze_csv(filepath):
    """分析 CSV 文件并打印统计信息"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            rows = list(reader)

            if not rows:
                print("CSV 文件为空")
                return

            print(f"\n文件: {filepath}")
            print(f"总行数: {len(rows)}")
            print("\n各列统计:")
            print("-" * 60)

            for column in rows[0].keys():
                values = [row[column] for row in rows]
                non_empty = [v for v in values if v.strip()]
                unique = set(non_empty)

                print(f"\n列名: {column}")
                print(f"  非空数: {len(non_empty)}/{len(values)}")
                print(f"  唯一值数: {len(unique)}")

                # 如果唯一值不多，显示前几个
                if len(unique) <= 5:
                    print(f"  唯一值: {', '.join(str(v) for v in list(unique)[:5])}")

    except FileNotFoundError:
        print(f"错误: 找不到文件 {filepath}")
    except Exception as e:
        print(f"错误: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python csv_stats.py <csv文件路径>")
        print("示例: python csv_stats.py sample.csv")
        sys.exit(1)

    csv_file = sys.argv[1]
    analyze_csv(csv_file)
