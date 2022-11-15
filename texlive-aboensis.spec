Name:		texlive-aboensis
Version:	62977
Release:	1
Summary:	A late medieval OpenType cursive font
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/aboensis
License:	ofl lppl1.3c cc-by-4 pd
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/aboensis.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/aboensis.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package contains the free OpenType medieval cursive font
Aboensis and a style file to use it in XeLaTeX documents. The
font is based on Codex Aboensis, that is a law book written in
Sweden in the 1430s. Since medieval cursive is very difficult
to read for modern people, the font is not suitable for use as
an ordinary book font, but is intended for emulating late
medieval manuscripts. The font contains two sets of initials:
Lombardic and cursive to go with the basic alphabet, and there
is support for writing two-colored initials and capitals. There
are also a large number of abbreviation sigla that can be
accessed as ligature substitutions. The style file contains
macros that help to use the extended features of the font such
as initials and two-colored capitals. There are also macros to
help achieve even pages with consistent line spacing.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/aboensis
%{_texmfdistdir}/fonts/opentype/public/aboensis
%doc %{_texmfdistdir}/doc/fonts/aboensis

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
