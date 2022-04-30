(org-babel-load-file
 (expand-file-name
  "config.org"
  user-emacs-directory))

(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(ansi-color-faces-vector
   [default default default italic underline success warning error])
 '(ansi-color-names-vector
   ["#292D3E" "#ff5370" "#c3e88d" "#ffcb6b" "#82aaff" "#c792ea" "#89DDFF" "#EEFFFF"])
 '(awesome-tray-mode-line-active-color "#2fafff")
 '(awesome-tray-mode-line-inactive-color "#323232")
 '(beacon-color "#cc6666")
 '(confirm-kill-emacs 'y-or-n-p)
 '(custom-enabled-themes '(doom-city-lights))
 '(custom-safe-themes
   '("1b8d67b43ff1723960eb5e0cba512a2c7a2ad544ddb2533a90101fd1852b426e" "1f1b545575c81b967879a5dddc878783e6ebcca764e4916a270f9474215289e5" "7a7b1d475b42c1a0b61f3b1d1225dd249ffa1abb1b7f726aec59ac7ca3bf4dae" "c5ded9320a346146bbc2ead692f0c63be512747963257f18cc8518c5254b7bf5" "6c531d6c3dbc344045af7829a3a20a09929e6c41d7a7278963f7d3215139f6a7" "8d7b028e7b7843ae00498f68fad28f3c6258eda0650fe7e17bfb017d51d0e2a2" "3d47380bf5aa650e7b8e049e7ae54cdada54d0637e7bac39e4cc6afb44e8463b" "cbdf8c2e1b2b5c15b34ddb5063f1b21514c7169ff20e081d39cf57ffee89bc1e" "e6f3a4a582ffb5de0471c9b640a5f0212ccf258a987ba421ae2659f1eaa39b09" "1704976a1797342a1b4ea7a75bdbb3be1569f4619134341bd5a4c1cfb16abad4" "745d03d647c4b118f671c49214420639cb3af7152e81f132478ed1c649d4597d" "84b14a0a41bb2728568d40c545280dbe7d6891221e7fbe7c2b1c54a3f5959289" "b5803dfb0e4b6b71f309606587dd88651efe0972a5be16ece6a958b197caeed8" "028c226411a386abc7f7a0fba1a2ebfae5fe69e2a816f54898df41a6a3412bb5" "353ffc8e6b53a91ac87b7e86bebc6796877a0b76ddfc15793e4d7880976132ae" "0d01e1e300fcafa34ba35d5cf0a21b3b23bc4053d388e352ae6a901994597ab1" "a6e620c9decbea9cac46ea47541b31b3e20804a4646ca6da4cce105ee03e8d0e" "c2aeb1bd4aa80f1e4f95746bda040aafb78b1808de07d340007ba898efa484f5" "246a9596178bb806c5f41e5b571546bb6e0f4bd41a9da0df5dfbca7ec6e2250c" "d6844d1e698d76ef048a53cefe713dbbe3af43a1362de81cdd3aefa3711eae0d" "6c98bc9f39e8f8fd6da5b9c74a624cbb3782b4be8abae8fd84cbc43053d7c175" "234dbb732ef054b109a9e5ee5b499632c63cc24f7c2383a849815dacc1727cb6" "c4063322b5011829f7fdd7509979b5823e8eea2abf1fe5572ec4b7af1dd78519" "4b6b6b0a44a40f3586f0f641c25340718c7c626cbf163a78b5a399fbe0226659" "628278136f88aa1a151bb2d6c8a86bf2b7631fbea5f0f76cba2a0079cd910f7d" "bb08c73af94ee74453c90422485b29e5643b73b05e8de029a6909af6a3fb3f58" "82d2cac368ccdec2fcc7573f24c3f79654b78bf133096f9b40c20d97ec1d8016" "43f03c7bf52ec64cdf9f2c5956852be18c69b41c38ab5525d0bedfbd73619b6a" "4aee8551b53a43a883cb0b7f3255d6859d766b6c5e14bcb01bed572fcbef4328" "06f0b439b62164c6f8f84fdda32b62fb50b6d00e8b01c2208e55543a6337433a" "bf798e9e8ff00d4bf2512597f36e5a135ce48e477ce88a0764cfb5d8104e8163" "36ca8f60565af20ef4f30783aa16a26d96c02df7b4e54e9900a5138fb33808da" "c9ddf33b383e74dac7690255dd2c3dfa1961a8e8a1d20e401c6572febef61045" "5e3fc08bcadce4c6785fc49be686a4a82a356db569f55d411258984e952f194a" "7153b82e50b6f7452b4519097f880d968a6eaf6f6ef38cc45a144958e553fbc6" "ab04c00a7e48ad784b52f34aa6bfa1e80d0c3fcacc50e1189af3651013eb0d58" "7356632cebc6a11a87bc5fcffaa49bae528026a78637acd03cae57c091afd9b9" "04dd0236a367865e591927a3810f178e8d33c372ad5bfef48b5ce90d4b476481" "a0feb1322de9e26a4d209d1cfa236deaf64662bb604fa513cca6a057ddf0ef64" "0466adb5554ea3055d0353d363832446cd8be7b799c39839f387abb631ea0995" "850bb46cc41d8a28669f78b98db04a46053eca663db71a001b40288a9b36796c" "835868dcd17131ba8b9619d14c67c127aa18b90a82438c8613586331129dda63" "a7b20039f50e839626f8d6aa96df62afebb56a5bbd1192f557cb2efb5fcfb662" "f7fed1aadf1967523c120c4c82ea48442a51ac65074ba544a5aefc5af490893b" "da53441eb1a2a6c50217ee685a850c259e9974a8fa60e899d393040b4b8cc922" "fe2539ccf78f28c519541e37dc77115c6c7c2efcec18b970b16e4a4d2cd9891d" "4b0e826f58b39e2ce2829fab8ca999bcdc076dec35187bf4e9a4b938cb5771dc" "a0be7a38e2de974d1598cf247f607d5c1841dbcef1ccd97cded8bea95a7c7639" "846b3dc12d774794861d81d7d2dcdb9645f82423565bfb4dad01204fa322dbd5" "a82ab9f1308b4e10684815b08c9cac6b07d5ccb12491f44a942d845b406b0296" "da186cce19b5aed3f6a2316845583dbee76aea9255ea0da857d1c058ff003546" "5784d048e5a985627520beb8a101561b502a191b52fa401139f4dd20acb07607" "97db542a8a1731ef44b60bc97406c1eb7ed4528b0d7296997cbb53969df852d6" "76ed126dd3c3b653601ec8447f28d8e71a59be07d010cd96c55794c3008df4d7" "67f0f440afa2e68d9d00219b5a56308761af45832fb60769d2b2fd36e3fead45" "aba75724c5d4d0ec0de949694bce5ce6416c132bb031d4e7ac1c4f2dbdd3d580" "8146edab0de2007a99a2361041015331af706e7907de9d6a330a3493a541e5a6" "afeb7b07dbc1a4cfadb24f3ef6c8cf5e63051bf76411779f03a0fe3aadc07768" "a53f00556ab4c81a0618ab6589053d9e351312d37d9c9cf544e0c8edac2b63ab" "88deeaaab5a631834e6f83e8359b571cfcbf5a18b04990288c8569cc16ee0798" "d0fb0c463d5d61e93f920e0fd1aa4c023bf719874b4d08f7f473b46c4adc0682" "6fc03df7304728b1346091dd6737cb0379f348ddc9c307f8b410fba991b3e475" "4699e3a86b1863bbc695236036158d175a81f0f3ea504e2b7c71f8f7025e19e3" "1278c5f263cdb064b5c86ab7aa0a76552082cf0189acf6df17269219ba496053" "6f4421bf31387397f6710b6f6381c448d1a71944d9e9da4e0057b3fe5d6f2fad" "4a5aa2ccb3fa837f322276c060ea8a3d10181fecbd1b74cb97df8e191b214313" "e19ac4ef0f028f503b1ccafa7c337021834ce0d1a2bca03fcebc1ef635776bea" "a9a67b318b7417adbedaab02f05fa679973e9718d9d26075c6235b1f0db703c8" "613aedadd3b9e2554f39afe760708fc3285bf594f6447822dd29f947f0775d6c" "d268b67e0935b9ebc427cad88ded41e875abfcc27abd409726a92e55459e0d01" "4f1d2476c290eaa5d9ab9d13b60f2c0f1c8fa7703596fa91b235db7f99a9441b" "b186688fbec5e00ee8683b9f2588523abdf2db40562839b2c5458fcfb322c8a4" "f91395598d4cb3e2ae6a2db8527ceb83fed79dbaf007f435de3e91e5bda485fb" "5f19cb23200e0ac301d42b880641128833067d341d22344806cdad48e6ec62f6" "1d5e33500bc9548f800f9e248b57d1b2a9ecde79cb40c0b1398dec51ee820daf" "f6665ce2f7f56c5ed5d91ed5e7f6acb66ce44d0ef4acfaa3a42c7cfe9e9a9013" "cf922a7a5c514fad79c483048257c5d8f242b21987af0db813d3f0b138dfaf53" "1bddd01e6851f5c4336f7d16c56934513d41cc3d0233863760d1798e74809b4b" "1d44ec8ec6ec6e6be32f2f73edf398620bb721afeed50f75df6b12ccff0fbb15" "e2c926ced58e48afc87f4415af9b7f7b58e62ec792659fcb626e8cba674d2065" "9b54ba84f245a59af31f90bc78ed1240fca2f5a93f667ed54bbf6c6d71f664ac" "47db50ff66e35d3a440485357fb6acb767c100e135ccdf459060407f8baea7b2" "266ecb1511fa3513ed7992e6cd461756a895dcc5fef2d378f165fed1c894a78c" "333958c446e920f5c350c4b4016908c130c3b46d590af91e1e7e2a0611f1e8c5" default))
 '(diary-entry-marker 'font-lock-variable-name-face)
 '(emms-mode-line-icon-color "#1ba1a1")
 '(exwm-floating-border-color "#232635")
 '(fci-rule-color "#676E95")
 '(flycheck-color-mode-line-face-to-color 'mode-line-buffer-id)
 '(flymake-error-bitmap '(flymake-double-exclamation-mark modus-themes-fringe-red))
 '(flymake-note-bitmap '(exclamation-mark modus-themes-fringe-cyan))
 '(flymake-warning-bitmap '(exclamation-mark modus-themes-fringe-yellow))
 '(frame-background-mode 'dark)
 '(frame-resize-pixelwise t)
 '(gnus-logo-colors '("#4c8383" "#bababa") t)
 '(gnus-mode-line-image-cache
   '(image :type xpm :ascent center :data "/* XPM */
static char *gnus-pointer[] = {
/* width height num_colors chars_per_pixel */
\"    18    13        2            1\",
/* colors */
\". c #1ba1a1\",
\"# c None s None\",
/* pixels */
\"##################\",
\"######..##..######\",
\"#####........#####\",
\"#.##.##..##...####\",
\"#...####.###...##.\",
\"#..###.######.....\",
\"#####.########...#\",
\"###########.######\",
\"####.###.#..######\",
\"######..###.######\",
\"###....####.######\",
\"###..######.######\",
\"###########.######\" };"))
 '(highlight-indent-guides-method 'character)
 '(highlight-tail-colors ((("#383f45") . 0) (("#323e51") . 20)))
 '(hl-sexp-background-color "#33323e")
 '(hl-todo-keyword-faces
   '(("HOLD" . "#c0c530")
     ("TODO" . "#feacd0")
     ("NEXT" . "#b6a0ff")
     ("THEM" . "#f78fe7")
     ("PROG" . "#00d3d0")
     ("OKAY" . "#4ae2f0")
     ("DONT" . "#70b900")
     ("FAIL" . "#ff8059")
     ("BUG" . "#ff8059")
     ("DONE" . "#44bc44")
     ("NOTE" . "#d3b55f")
     ("KLUDGE" . "#d0bc00")
     ("HACK" . "#d0bc00")
     ("TEMP" . "#ffcccc")
     ("FIXME" . "#ff9077")
     ("XXX+" . "#ef8b50")
     ("REVIEW" . "#6ae4b9")
     ("DEPRECATED" . "#bfd9ff")))
 '(ibuffer-deletion-face 'modus-themes-mark-del)
 '(ibuffer-filter-group-name-face 'modus-themes-pseudo-header)
 '(ibuffer-marked-face 'modus-themes-mark-sel)
 '(ibuffer-title-face 'default)
 '(jdee-db-active-breakpoint-face-colors (cons "#1c1f2b" "#c792ea"))
 '(jdee-db-requested-breakpoint-face-colors (cons "#1c1f2b" "#c3e88d"))
 '(jdee-db-spec-breakpoint-face-colors (cons "#1c1f2b" "#676E95"))
 '(line-number-mode nil)
 '(mode-line-percent-position nil)
 '(ns-command-modifier 'meta)
 '(objed-cursor-color "#ff5370")
 '(org-agenda-files nil)
 '(org-babel-load-languages '((python . t) (emacs-lisp . t)))
 '(org-src-block-faces 'nil)
 '(package-selected-packages
   '(multiple-cursors xah-fly-keys org-roam-timestamps org-roam-ui org-roam company-auctex treemacs-all-the-icons treemacs-projectile treemacs-magit treemacs-evil treemacs tree-sitter-langs tree-sitter go-mode elcord auctex-latexmk auctex color-theme-sanityinc-solarized color-theme-sanityinc-tomorrow badger-theme ample-theme alect-themes crux leuven-theme moe-theme modus-themes beacon rainbow-mode apheleia aggressive-indent telephone-line pandoc-mode chess osx-trash vterm-toggle polymode pretty-mode highlight-indent-guides python-mode lsp-pyright dmenu flyspell-correct-ivy flyspell-correct company rustic lsp-mode emojify LaTeX-mode writeroom-mode perspective neotree evil-tutor elfeed-goodies sudo-edit ox-man dired smex org-tempo all-the-icons-dired which-key vterm use-package toc-org projectile peep-dired org-bullets magit-todos magit-lfs ivy-rich ivy-posframe haskell-mode general evil-collection eshell-syntax-highlighting doom-themes doom-modeline dired-open dashboard counsel))
 '(pdf-view-midnight-colors (cons "#EEFFFF" "#292D3E"))
 '(persp-mode t)
 '(rustic-ansi-faces
   ["#292D3E" "#ff5370" "#c3e88d" "#ffcb6b" "#82aaff" "#c792ea" "#89DDFF" "#EEFFFF"])
 '(rustic-cargo-run-use-comint t)
 '(vc-annotate-background "#292D3E")
 '(vc-annotate-background-mode nil)
 '(vc-annotate-color-map
   (list
    (cons 20 "#c3e88d")
    (cons 40 "#d7de81")
    (cons 60 "#ebd476")
    (cons 80 "#ffcb6b")
    (cons 100 "#fcb66b")
    (cons 120 "#f9a16b")
    (cons 140 "#f78c6c")
    (cons 160 "#e78e96")
    (cons 180 "#d690c0")
    (cons 200 "#c792ea")
    (cons 220 "#d97dc1")
    (cons 240 "#ec6898")
    (cons 260 "#ff5370")
    (cons 280 "#d95979")
    (cons 300 "#b36082")
    (cons 320 "#8d678b")
    (cons 340 "#676E95")
    (cons 360 "#676E95")))
 '(vc-annotate-very-old-color nil)
 '(whitespace-style
   '(face trailing tabs spaces newline empty indentation space-after-tab space-before-tab space-mark tab-mark newline-mark))
 '(window-divider-mode nil)
 '(xterm-color-names
   ["black" "#ff8059" "#44bc44" "#d0bc00" "#2fafff" "#feacd0" "#00d3d0" "gray65"])
 '(xterm-color-names-bright
   ["gray35" "#ef8b50" "#70b900" "#c0c530" "#79a8ff" "#f78fe7" "#4ae2f0" "white"]))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(line-number ((t (:inherit default :background "alternatingContentBackgroundColor" :foreground "#a8a8a8" :strike-through nil :underline nil :slant normal :weight normal)))))
