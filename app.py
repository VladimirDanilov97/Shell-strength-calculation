from flask import Flask, request, render_template
from calculator import Shell
from forms import ShellForm
app = Flask(__name__)
app.config.from_object('config')


@app.route('/shell', methods=['GET','POST'])
def shell():
    form = ShellForm()
    context = {'form': form, 'Sr': None, 'd0r': None, 
               'k_zap': None, 'title': "Расчет обечайки"}
 
    if form.validate_on_submit():
        sh = Shell()
        sh.set_P(float(form.P.data))
        sh.set_T(float(form.T.data))
        sh.set_Dvn(float(form.Dvn.data))
        sh.set_steel(form.steel.data)
        sh.set_S(float(form.S.data))
        sh.set_C(float(form.C.data))
        sh.set_phi(float(form.phi.data))
        Sr = sh.calculate_Sr()
        context['Sr'] = Sr
        context['d0r'] = sh.calculate_unreinforced_hole()
        context['k_zap'] = sh.calculate_k_zap()
    return render_template('shell.html', **context)
    


if __name__ == '__main__':
    app.run(debug=True)