package iagoav.iewiki.multipleView;

import android.view.View;
import android.widget.LinearLayout;

import androidx.constraintlayout.widget.ConstraintLayout;

public interface MultipleViewAdapter {

    public int getItemCount();

    public View getView();

    public LinearLayout getRootLayout();
}
