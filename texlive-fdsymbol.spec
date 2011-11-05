# revision 23797
# category Package
# catalog-ctan /fonts/fdsymbol
# catalog-date 2011-08-30 14:04:46 +0200
# catalog-license lppl
# catalog-version 0.7
Name:		texlive-fdsymbol
Version:	0.7
Release:	1
Summary:	A maths symbol font
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/fdsymbol
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fdsymbol.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fdsymbol.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fdsymbol.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
FdSymbol is a maths symbol font, designed as a companion to the
Fedra family by Typotheque, but it might also fit other
contemporary typefaces.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/enc/dvips/fdsymbol/fdsymbol-a.enc
%{_texmfdistdir}/fonts/enc/dvips/fdsymbol/fdsymbol-b.enc
%{_texmfdistdir}/fonts/enc/dvips/fdsymbol/fdsymbol-c.enc
%{_texmfdistdir}/fonts/enc/dvips/fdsymbol/fdsymbol-d.enc
%{_texmfdistdir}/fonts/enc/dvips/fdsymbol/fdsymbol-e.enc
%{_texmfdistdir}/fonts/enc/dvips/fdsymbol/fdsymbol-f.enc
%{_texmfdistdir}/fonts/map/dvips/fdsymbol/fdsymbol.map
%{_texmfdistdir}/fonts/source/public/fdsymbol/FdSymbolA-Bold.mf
%{_texmfdistdir}/fonts/source/public/fdsymbol/FdSymbolA-Book.mf
%{_texmfdistdir}/fonts/source/public/fdsymbol/FdSymbolA-Medium.mf
%{_texmfdistdir}/fonts/source/public/fdsymbol/FdSymbolA-Regular.mf
%{_texmfdistdir}/fonts/source/public/fdsymbol/FdSymbolA.mf
%{_texmfdistdir}/fonts/source/public/fdsymbol/FdSymbolB-Bold.mf
%{_texmfdistdir}/fonts/source/public/fdsymbol/FdSymbolB-Book.mf
%{_texmfdistdir}/fonts/source/public/fdsymbol/FdSymbolB-Medium.mf
%{_texmfdistdir}/fonts/source/public/fdsymbol/FdSymbolB-Regular.mf
%{_texmfdistdir}/fonts/source/public/fdsymbol/FdSymbolB.mf
%{_texmfdistdir}/fonts/source/public/fdsymbol/FdSymbolC-Bold.mf
%{_texmfdistdir}/fonts/source/public/fdsymbol/FdSymbolC-Book.mf
%{_texmfdistdir}/fonts/source/public/fdsymbol/FdSymbolC-Medium.mf
%{_texmfdistdir}/fonts/source/public/fdsymbol/FdSymbolC-Regular.mf
%{_texmfdistdir}/fonts/source/public/fdsymbol/FdSymbolC.mf
%{_texmfdistdir}/fonts/source/public/fdsymbol/FdSymbolD-Bold.mf
%{_texmfdistdir}/fonts/source/public/fdsymbol/FdSymbolD-Book.mf
%{_texmfdistdir}/fonts/source/public/fdsymbol/FdSymbolD-Medium.mf
%{_texmfdistdir}/fonts/source/public/fdsymbol/FdSymbolD-Regular.mf
%{_texmfdistdir}/fonts/source/public/fdsymbol/FdSymbolD.mf
%{_texmfdistdir}/fonts/source/public/fdsymbol/FdSymbolE-Bold.mf
%{_texmfdistdir}/fonts/source/public/fdsymbol/FdSymbolE-Book.mf
%{_texmfdistdir}/fonts/source/public/fdsymbol/FdSymbolE-Medium.mf
%{_texmfdistdir}/fonts/source/public/fdsymbol/FdSymbolE-Regular.mf
%{_texmfdistdir}/fonts/source/public/fdsymbol/FdSymbolE.mf
%{_texmfdistdir}/fonts/source/public/fdsymbol/FdSymbolF-Bold.mf
%{_texmfdistdir}/fonts/source/public/fdsymbol/FdSymbolF-Book.mf
%{_texmfdistdir}/fonts/source/public/fdsymbol/FdSymbolF-Medium.mf
%{_texmfdistdir}/fonts/source/public/fdsymbol/FdSymbolF-Regular.mf
%{_texmfdistdir}/fonts/source/public/fdsymbol/FdSymbolF.mf
%{_texmfdistdir}/fonts/source/public/fdsymbol/fdaccents.mf
%{_texmfdistdir}/fonts/source/public/fdsymbol/fdarrows.mf
%{_texmfdistdir}/fonts/source/public/fdsymbol/fdbase.mf
%{_texmfdistdir}/fonts/source/public/fdsymbol/fddelims.mf
%{_texmfdistdir}/fonts/source/public/fdsymbol/fdgeometric.mf
%{_texmfdistdir}/fonts/source/public/fdsymbol/fdoperators.mf
%{_texmfdistdir}/fonts/source/public/fdsymbol/fdrelations.mf
%{_texmfdistdir}/fonts/source/public/fdsymbol/fdturnstile.mf
%{_texmfdistdir}/fonts/tfm/public/fdsymbol/FdSymbolA-Bold.tfm
%{_texmfdistdir}/fonts/tfm/public/fdsymbol/FdSymbolA-Book.tfm
%{_texmfdistdir}/fonts/tfm/public/fdsymbol/FdSymbolA-Medium.tfm
%{_texmfdistdir}/fonts/tfm/public/fdsymbol/FdSymbolA-Regular.tfm
%{_texmfdistdir}/fonts/tfm/public/fdsymbol/FdSymbolB-Bold.tfm
%{_texmfdistdir}/fonts/tfm/public/fdsymbol/FdSymbolB-Book.tfm
%{_texmfdistdir}/fonts/tfm/public/fdsymbol/FdSymbolB-Medium.tfm
%{_texmfdistdir}/fonts/tfm/public/fdsymbol/FdSymbolB-Regular.tfm
%{_texmfdistdir}/fonts/tfm/public/fdsymbol/FdSymbolC-Bold.tfm
%{_texmfdistdir}/fonts/tfm/public/fdsymbol/FdSymbolC-Book.tfm
%{_texmfdistdir}/fonts/tfm/public/fdsymbol/FdSymbolC-Medium.tfm
%{_texmfdistdir}/fonts/tfm/public/fdsymbol/FdSymbolC-Regular.tfm
%{_texmfdistdir}/fonts/tfm/public/fdsymbol/FdSymbolD-Bold.tfm
%{_texmfdistdir}/fonts/tfm/public/fdsymbol/FdSymbolD-Book.tfm
%{_texmfdistdir}/fonts/tfm/public/fdsymbol/FdSymbolD-Medium.tfm
%{_texmfdistdir}/fonts/tfm/public/fdsymbol/FdSymbolD-Regular.tfm
%{_texmfdistdir}/fonts/tfm/public/fdsymbol/FdSymbolE-Bold.tfm
%{_texmfdistdir}/fonts/tfm/public/fdsymbol/FdSymbolE-Book.tfm
%{_texmfdistdir}/fonts/tfm/public/fdsymbol/FdSymbolE-Medium.tfm
%{_texmfdistdir}/fonts/tfm/public/fdsymbol/FdSymbolE-Regular.tfm
%{_texmfdistdir}/fonts/tfm/public/fdsymbol/FdSymbolF-Bold.tfm
%{_texmfdistdir}/fonts/tfm/public/fdsymbol/FdSymbolF-Book.tfm
%{_texmfdistdir}/fonts/tfm/public/fdsymbol/FdSymbolF-Medium.tfm
%{_texmfdistdir}/fonts/tfm/public/fdsymbol/FdSymbolF-Regular.tfm
%{_texmfdistdir}/fonts/type1/public/fdsymbol/FdSymbol-Bold.pfb
%{_texmfdistdir}/fonts/type1/public/fdsymbol/FdSymbol-Book.pfb
%{_texmfdistdir}/fonts/type1/public/fdsymbol/FdSymbol-Medium.pfb
%{_texmfdistdir}/fonts/type1/public/fdsymbol/FdSymbol-Regular.pfb
%{_texmfdistdir}/tex/latex/fdsymbol/fdsymbol.sty
%doc %{_texmfdistdir}/doc/fonts/fdsymbol/FONTLOG.txt
%doc %{_texmfdistdir}/doc/fonts/fdsymbol/OFL.txt
%doc %{_texmfdistdir}/doc/latex/fdsymbol/fdsymbol.pdf
#- source
%doc %{_texmfdistdir}/source/latex/fdsymbol/fdsymbol.dtx
%doc %{_texmfdistdir}/source/latex/fdsymbol/fdsymbol.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
