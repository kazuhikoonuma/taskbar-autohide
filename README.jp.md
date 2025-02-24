このツールは "ツール バーは、既に画面のこの端に隠れています。" の回避策です。  
[ダウンロードはこちら](https://github.com/kazuhikoonuma/taskbar-autohide/releases)

[English version is here](https://github.com/kazuhikoonuma/taskbar-autohide/blob/main/README.md)

## 動機

![dialog](https://raw.githubusercontent.com/kazuhikoonuma/taskbar-autohide/refs/heads/main/resources/dialog.png)

> ツール バーは、既に画面のこの端に隠れています。  
> 画面の各端に置ける隠しツール バーは、それぞれ 1 つです。

私のノートPCには OLED ディスプレイが搭載されています。焼き付き防止のために、タスクバーを常に非表示にしておきたいのですが、スリープから復帰するとタスクバーの自動非表示機能が無効になってしまうことがあります。設定画面から手動で再有効化するのは面倒なので、タスクバーを監視し、自動的に再有効化するツールを作成しました。

## 機能

- **タスクバーの自動非表示**: 無効になった場合、自動的に再有効化します。
- **システムトレイアイコン**: プログラムの状態を視覚的に表示します。
- **通知システム**: タスクバーの自動非表示機能が再有効化された際に通知します。
- **多重起動の防止**: 1つのインスタンスのみが実行されるようにします。

## 使い方

### 簡単な使い方

1. [Releases](https://github.com/kazuhikoonuma/taskbar-autohide/releases) ページから最新のリリースをダウンロード。
2. 実行ファイルを起動。

### 高度な使い方

1. 実行ファイルをダウンロード。
2. `shell:startup` を開き、実行ファイルへのショートカットをスタートアップディレクトリに配置。
3. Windows にログインすると、自動的にプログラムが起動。

## 動作原理

このプログラムは、タスクバーの自動非表示機能を10秒ごとにポーリングし、無効になっていた場合に自動的に再有効化します。バックグラウンドで動作し、システムトレイアイコンからアクセスできます。

## 動作確認環境

- Windows 11 Pro (24H2)
- Python 3.13

## ビルド手順

```bash
pip install -r resources/requirements.txt
pyinstaller resources/autohide.spec
```

ビルド後、実行ファイルは `dist` ディレクトリに生成されます。

## リポジトリ

[GitHub](https://github.com/kazuhikoonuma/taskbar-autohide)

## ライセンス

このプロジェクトは MIT ライセンスのもとで公開されています。詳細については [LICENSE](https://github.com/kazuhikoonuma/taskbar-autohide/blob/main/LICENSE) を参照してください。

## サードパーティーライセンス

このプロジェクトでは、以下のサードパーティライブラリを利用させていただいております。

- [**cairosvg**](https://github.com/Kozea/CairoSVG): LGPL-3.0
- [**Pillow (PIL)**](https://github.com/python-pillow/Pillow): MIT-CMU
- [**pystray**](https://github.com/moses-palmer/pystray): GPL-3.0 or LGPL-3.0 (デュアルライセンス)
- [**tendo**](https://github.com/pycontribs/tendo): PSF-2.0
- [**winotify**](https://github.com/versa-syahptr/winotify): MIT
- [**PyInstaller**](https://github.com/pyinstaller/pyinstaller): GPL-2.0-or-later with Bootloader Exception (コア部分); ランタイムフックは Apache License 2.0; 分離モジュールは MIT ライセンス。

各ライブラリの公式ライセンス文書を参照してください。

## サポート

私はしょっちゅうこの現象に遭遇し、そのたびに「んもーまたタスクバー復活しとる…」と困っていました。  
それが今ではこのツールによって「Autohide is disabled. Re-enabling...」という通知が出るたびに満足感と達成感に包まれています笑  

このプロジェクトが同じ問題で困っている皆さんのお役に立てることを願っています。もしサポートしていただける場合は、以下のリンクをご利用ください。
[![ko-fi](https://raw.githubusercontent.com/kazuhikoonuma/taskbar-autohide/refs/heads/main/resources/support_me_on_kofi_dark.png)](https://ko-fi.com/kazuhikoonuma)
