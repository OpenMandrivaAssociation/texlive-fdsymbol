%global tl_name fdsymbol
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	A maths symbol font
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/fdsymbol
License:	ofl lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fdsymbol.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fdsymbol.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fdsymbol.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
FdSymbol is a maths symbol font, designed as a companion to the Fedra
family by Typotheque, but it might also fit other contemporary
typefaces.

