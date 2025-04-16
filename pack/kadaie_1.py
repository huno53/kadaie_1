# 課題E-1
import argparse
import gzip
import os
import re


# pdb_seqres.txt.gzを読み込む
def extract_gzip(filename):
    # ファイルパスを展開
    filename = os.path.expanduser(filename)
    # gzipを展開して内容を格納
    with gzip.open(filename, "rt") as file:
        data = file.read()
    return data


# 各エントリーのlengthを取得
def get_lengths(data):
    lengths = [int(length) for length in re.findall(r"length:(\d+)", data)]
    return lengths


# 長さ100以上の配列を数える
def longer_than(lengths, threshold):
    count = sum(1 for num in lengths if num >= threshold)
    return count


def main():
    # コマンドライン引数を解析
    parser = argparse.ArgumentParser(description="残基数の割合を計算するツール")
    parser.add_argument("-i", "--input", required=True, help="入力ファイル (gzip形式)")
    parser.add_argument(
        "-l", "--length", type=int, required=True, help="閾値となる長さ"
    )
    args = parser.parse_args()

    # ファイルを読み込む
    data = extract_gzip(args.input)

    # 計算
    allrecords = data.count(">")
    lengths = get_lengths(data)
    longer_records = longer_than(lengths, args.length)

    # 結果を表示
    print(f"全てのレコード数: {allrecords}")
    print(f"長さ{args.length}以上の配列の数: {longer_records}")
    print(f"長さ{args.length}以上の配列の割合: {longer_records / allrecords:.1%}")


if __name__ == "__main__":
    main()
